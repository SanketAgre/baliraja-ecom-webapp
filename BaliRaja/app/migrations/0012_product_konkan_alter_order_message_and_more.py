# Generated by Django 4.0.4 on 2022-05-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='konkan',
            field=models.BooleanField(default=False, help_text='0=default, 1=konkan'),
        ),
        migrations.AlterField(
            model_name='order',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
