# Generated by Django 4.2.2 on 2023-07-18 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='user',
        ),
    ]
