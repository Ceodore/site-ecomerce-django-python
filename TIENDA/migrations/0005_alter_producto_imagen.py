# Generated by Django 3.2.4 on 2021-06-20 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TIENDA', '0004_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes'),
        ),
    ]
