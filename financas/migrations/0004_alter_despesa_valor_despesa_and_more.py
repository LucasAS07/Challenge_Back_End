# Generated by Django 4.1 on 2022-08-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0003_despesa_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='valor_despesa',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='receita',
            name='valor_receita',
            field=models.FloatField(),
        ),
    ]