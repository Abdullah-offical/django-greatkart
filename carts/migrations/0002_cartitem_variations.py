# Generated by Django 5.0.6 on 2024-07-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0001_initial"),
        ("store", "0002_variation"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="variations",
            field=models.ManyToManyField(blank=True, to="store.variation"),
        ),
    ]
