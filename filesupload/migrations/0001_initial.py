# Generated by Django 4.1.5 on 2023-01-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Shop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nomeDaLoja", models.CharField(max_length=25)),
                ("donoDaLoja", models.CharField(max_length=25)),
            ],
        ),
    ]