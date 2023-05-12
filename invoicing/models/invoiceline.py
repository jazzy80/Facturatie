from django.db import models

from invoicing.models import Product, Invoice


class InvoiceLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    invoice = models.ForeignKey(Invoice, related_name='lines', on_delete=models.CASCADE)
