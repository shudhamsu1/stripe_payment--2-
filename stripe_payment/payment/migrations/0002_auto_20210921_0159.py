# Generated by Django 3.2.7 on 2021-09-21 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amountpaid',
            name='bank',
        ),
        migrations.DeleteModel(
            name='CreditsSetting',
        ),
        migrations.RemoveField(
            model_name='paymentinformation',
            name='user',
        ),
        migrations.DeleteModel(
            name='AmountPaid',
        ),
        migrations.DeleteModel(
            name='PaymentInformation',
        ),
    ]
