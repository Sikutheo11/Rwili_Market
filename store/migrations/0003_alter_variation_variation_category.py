# Generated by Django 3.2.8 on 2021-10-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('size', 'size'), ('Igiti', 'Igiti')], max_length=100),
        ),
    ]
