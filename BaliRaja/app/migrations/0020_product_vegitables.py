# Generated by Django 4.0.4 on 2022-05-31 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_remove_category_best_deal_product_best_deal'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vegitables',
            field=models.BooleanField(default=False, help_text='0=default, 1=Vegitables'),
        ),
    ]
