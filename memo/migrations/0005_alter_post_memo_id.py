# Generated by Django 4.2.1 on 2023-05-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("memo", "0004_rename_id_post_memo_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="memo_id",
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
