from decimal import Decimal
from functools import reduce
from typing import Any, List, Optional, Tuple

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from invoicing.models import Product, Klant, Invoice, InvoiceLine


class BtwFilter(admin.SimpleListFilter):
    title = 'Btw Filter'
    parameter_name = 'Btw tarief'
    BTW_PERCENTAGE = 21

    def lookups(self, _: HttpRequest, __: admin.ModelAdmin) -> List[Tuple[str, str]]:
        return [(0, 'Laag'), (1, 'Hoog')]

    def queryset(self, _: HttpRequest, queryset: QuerySet[Product]) -> QuerySet[Product]:
        filter = {'btw__lt': self.BTW_PERCENTAGE} \
            if self.value() == '0' \
            else {'btw__gte': self.BTW_PERCENTAGE}
        return queryset.filter(**filter)


class InvoiceLine(admin.TabularInline):
    model = InvoiceLine


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'btw')
    search_fields = ('name',)
    list_filter = ('type', BtwFilter)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Product]:
        return super().get_queryset(request).order_by('name')


@admin.register(Klant)
class KlantAdmin(admin.ModelAdmin):
    pass


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    fields = ('date', 'klant', 'price_ex', 'btw', 'price')
    readonly_fields = ('price_ex', 'btw', 'price')
    inlines = [InvoiceLine]

    def generate_lines(self, invoice: Invoice) -> dict:
        def generate(acc: dict, line: InvoiceLine) -> dict:
            price = line.product.price
            price_ex = price / (1 + line.product.btw / 100)
            btw = price_ex * line.product.btw / 100
            acc['price_ex'] += price_ex
            acc['btw'] += btw
            acc['price'] += price
            return acc

        return reduce(
            generate,
            invoice.lines.all(),
            {
                'price_ex': Decimal(0),
                'btw': Decimal(0),
                'price': Decimal(0)
            }
        )

    def format_price(self, price: Decimal) -> str:
        return '{0:.2f}'.format(price)

    def btw(self, invoice: Invoice = None) -> Decimal:
        return self.format_price(self.generate_lines(invoice)['btw'])

    def price_ex(self, invoice: Invoice = None) -> Decimal:
        return self.format_price(self.generate_lines(invoice)['price_ex'])

    def price(self, invoice: Invoice = None) -> Decimal:
        return self.format_price(self.generate_lines(invoice)['price'])
