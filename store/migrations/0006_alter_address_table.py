# Generated by Django 4.2.3 on 2023-07-18 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_price_orderitem_unit_price'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='address',
            table='customer_address',
        ),
    ]
