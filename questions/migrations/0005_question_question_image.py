# Generated by Django 4.2.2 on 2023-08-05 12:29

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("questions", "0004_remove_question_question_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="question_image",
            field=models.TextField(default=1, verbose_name=builtins.max),
            preserve_default=False,
        ),
    ]
