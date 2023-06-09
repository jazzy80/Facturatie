# Generated by Django 4.2.1 on 2023-05-12 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0003_created_invoice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='klant',
            options={'verbose_name_plural': 'Klanten'},
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.IntegerField(choices=[(0, 'Onbekend'), (1, 'Product'), (2, 'Dienst')], default=0),
        ),
        migrations.AlterField(
            model_name='invoiceline',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='invoicing.invoice'),
        ),
    ]
