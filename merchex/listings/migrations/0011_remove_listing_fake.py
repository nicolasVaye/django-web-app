# Generated by Django 5.0.2 on 2024-02-16 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_listing_fake'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='fake',
        ),
    ]