# Generated by Django 4.2.7 on 2023-12-17 06:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("first", "0005_post_is_draft"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="dt",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
