# Generated by Django 4.0.4 on 2022-06-15 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_product_farming_tools'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='farming_product',
        ),
        migrations.AddField(
            model_name='product',
            name='other_farming_Tools',
            field=models.BooleanField(default=False, help_text='0=default, 1=Other_farming_Tools'),
        ),
    ]
