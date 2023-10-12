# Generated by Django 4.2.6 on 2023-10-11 14:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(limit_value=200000), django.core.validators.MinLengthValidator(limit_value=500)]),
        ),
    ]
