# Generated by Django 5.2.3 on 2025-06-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='keywords',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
