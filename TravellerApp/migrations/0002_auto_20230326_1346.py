# Generated by Django 3.2.18 on 2023-03-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravellerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='additional_info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='guide',
            field=models.TextField(blank=True),
        ),
    ]