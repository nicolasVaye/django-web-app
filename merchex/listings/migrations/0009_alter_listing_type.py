# Generated by Django 5.0.2 on 2024-02-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_alter_listing_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('R', 'Disques'), ('C', 'Vetements'), ('P', 'Affiches'), ('M', 'Divers')], max_length=5),
        ),
    ]
