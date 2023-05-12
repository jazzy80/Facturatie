from django.db import models


class Klant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, blank=True, null=True)
    adres = models.CharField(max_length=200)
    post_code = models.CharField(max_length=20)
    woonplaats = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name} - {self.email}'

    class Meta: 
        verbose_name_plural = "Klanten"