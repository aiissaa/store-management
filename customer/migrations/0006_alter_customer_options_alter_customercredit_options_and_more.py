# Generated by Django 4.1.7 on 2023-02-22 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_remove_customer_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='customercredit',
            options={'verbose_name': 'Crédit client', 'verbose_name_plural': 'Crédits clients'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Paiement', 'verbose_name_plural': 'Paiements'},
        ),
    ]
