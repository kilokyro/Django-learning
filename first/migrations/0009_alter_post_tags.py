# Generated by Django 4.2.7 on 2023-12-24 02:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("first", "0008_tag_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(blank=True, to="first.tag"),
        ),
    ]
