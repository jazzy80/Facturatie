# Generated by Django 4.2.1 on 2023-06-02 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0004_added_product_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='klant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='invoicing.klant'),
        ),
    ]