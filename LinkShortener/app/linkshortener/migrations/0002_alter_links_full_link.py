# Generated by Django 5.1.3 on 2024-11-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkshortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='full_link',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
