# Generated by Django 4.0.1 on 2022-01-23 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('created',)},
        ),
    ]
