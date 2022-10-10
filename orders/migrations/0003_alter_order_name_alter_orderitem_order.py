# Generated by Django 4.1.1 on 2022-09-25 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orders", "0002_alter_order_address_alter_order_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="name",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="orders.order",
            ),
        ),
    ]
