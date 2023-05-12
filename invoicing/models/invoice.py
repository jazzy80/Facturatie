from django.db import models

from invoicing.models.klant import Klant


class Invoice(models.Model):
    date = models.DateField()
    klant = models.ForeignKey(Klant, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.klant} - {self.date}'
