# Generated by Django 4.1.5 on 2023-03-26 01:20

import contracts_v2.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts_v2', '0020_evecontractexpectation_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evecontracttaxreport',
            name='end_range',
            field=models.DateField(default=contracts_v2.models.get_end_range),
        ),
        migrations.AlterField(
            model_name='evecontracttaxreport',
            name='start_range',
            field=models.DateField(default=contracts_v2.models.get_start_range),
        ),
    ]