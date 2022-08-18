# Generated by Django 4.1 on 2022-08-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0002_despesa'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='categoria',
            field=models.CharField(choices=[('A', 'Outros'), ('S', 'Saude'), ('M', 'Moradia'), ('T', 'Transporte'), ('E', 'Educação'), ('L', 'Lazer'), ('I', 'Imprevistos'), ('O', 'Outros')], default='O', max_length=1),
        ),
    ]