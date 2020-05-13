# Generated by Django 2.2.10 on 2020-03-17 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20200314_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='', help_text='Opis Produktu', max_length=150, verbose_name='OPIS'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='NAZWA PRODUKTU'),
        ),
        migrations.AlterField(
            model_name='product',
            name='prize',
            field=models.CharField(help_text='In zl', max_length=10, verbose_name='Cena jednostkowa'),
        ),
        migrations.AlterField(
            model_name='product',
            name='types',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='menu.TypeOfProduct', verbose_name='RODZAJ PRODUKTU'),
        ),
        migrations.AlterField(
            model_name='typeofproduct',
            name='amount',
            field=models.CharField(default='', help_text='In ml', max_length=15, verbose_name='Amount of liquor'),
        ),
        migrations.AlterField(
            model_name='typeofproduct',
            name='name',
            field=models.CharField(max_length=100, verbose_name='RODZAJ PRODUKTU'),
        ),
    ]