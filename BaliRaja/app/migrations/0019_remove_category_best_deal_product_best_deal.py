# Generated by Django 4.0.4 on 2022-05-31 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_category_best_deal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='best_deal',
        ),
        migrations.AddField(
            model_name='product',
            name='best_deal',
            field=models.BooleanField(default=False, help_text='0=default, 1=Best_deal'),
        ),
    ]
