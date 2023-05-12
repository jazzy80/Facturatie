from django.db import models


class ProductType(models.IntegerChoices):
    ONBEKEND = 0
    PRODUCT = 1
    DIENST = 2


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=14, decimal_places=10)
    btw = models.DecimalField(max_digits=6, decimal_places=4)
    image = models.CharField(blank=True, null=True)
    type = models.IntegerField(
        choices=ProductType.choices, default=ProductType.ONBEKEND)

    def __str__(self) -> str:
        return f'{self.name} - {self.price:0.2f}'
