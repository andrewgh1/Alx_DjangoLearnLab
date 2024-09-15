# Generated by Django 5.1.1 on 2024-09-15 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="created_date",
            new_name="created_at",
        ),
        migrations.AddField(
            model_name="comment",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="blog.post",
            ),
        ),
    ]
