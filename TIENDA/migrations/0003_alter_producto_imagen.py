# Generated by Django 3.2.4 on 2021-06-17 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TIENDA', '0002_auto_20210616_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='imagenes/'),
        ),
    ]
