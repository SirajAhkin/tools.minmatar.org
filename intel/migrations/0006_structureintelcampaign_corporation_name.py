# Generated by Django 4.1.5 on 2023-10-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel', '0005_alter_structureintel_alliance_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='structureintelcampaign',
            name='corporation_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]