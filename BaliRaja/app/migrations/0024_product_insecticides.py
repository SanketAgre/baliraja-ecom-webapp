# Generated by Django 4.0.4 on 2022-06-15 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_product_fertilizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='insecticides',
            field=models.BooleanField(default=False, help_text='0=default, 1=Insecticides'),
        ),
    ]
