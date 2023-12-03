# Generated by Django 4.2.5 on 2023-10-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_custom_delete_userlocation"),
    ]

    operations = [
        migrations.CreateModel(
            name="sell",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("mobile", models.CharField(max_length=20)),
                ("birthday", models.DateField()),
                ("occupation", models.CharField(max_length=255)),
                ("active", models.BooleanField(default=False)),
            ],
        ),
    ]
