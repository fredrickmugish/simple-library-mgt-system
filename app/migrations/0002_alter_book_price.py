# Generated by Django 5.0 on 2023-12-29 23:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="price",
            field=models.CharField(max_length=10),
        ),
    ]
