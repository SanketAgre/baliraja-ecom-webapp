# Generated by Django 4.0.4 on 2022-06-15 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_product_insecticides'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='farming_Tools',
            field=models.BooleanField(default=False, help_text='0=default, 1=Farming_Tools'),
        ),
    ]
