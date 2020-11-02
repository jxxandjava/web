# Generated by Django 2.2.4 on 2020-06-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('economy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversionrate',
            name='source',
            field=models.CharField(choices=[('cryptocompare', 'cryptocompare'), ('poloniex', 'poloniex'), ('uniswap', 'uniswap'), ('manual', 'manual')], db_index=True, max_length=30),
        ),
    ]