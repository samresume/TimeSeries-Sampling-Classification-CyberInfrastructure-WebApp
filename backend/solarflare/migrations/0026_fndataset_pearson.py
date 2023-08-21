# Generated by Django 4.1.5 on 2023-07-17 23:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarflare', '0025_dataset_znormalization_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fndataset',
            name='pearson',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-1.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]
