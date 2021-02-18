# Generated by Django 3.1.6 on 2021-02-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(blank=True, null=True)),
                (
                    "sold_price",
                    models.DecimalField(
                        blank=True, decimal_places=1000, max_digits=1000, null=True
                    ),
                ),
                ("bids", models.IntegerField(blank=True, null=True)),
                ("sold_date", models.DateField(blank=True, null=True)),
                ("card_link", models.TextField(blank=True, null=True)),
                ("image_link", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
