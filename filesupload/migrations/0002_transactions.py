# Generated by Django 4.1.5 on 2023-01-27 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("filesupload", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transactions",
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
                ("tipo", models.IntegerField()),
                ("data", models.CharField(max_length=16)),
                ("valor", models.DecimalField(decimal_places=2, max_digits=15)),
                ("cpf", models.CharField(max_length=12)),
                ("cartão", models.CharField(max_length=12)),
                ("hora", models.CharField(max_length=12)),
                (
                    "shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transacoes",
                        to="filesupload.shop",
                    ),
                ),
            ],
        ),
    ]