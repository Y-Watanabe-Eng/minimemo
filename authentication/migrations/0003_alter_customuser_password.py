# Generated by Django 4.2.2 on 2023-07-17 10:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_customuser_password_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Passwordは大文字・小文字・数字・記号のうち少なくとも2種類を含める必要があります。', regex='^(?=.*?[a-z])(?=.*?[0-9]).*$')]),
        ),
    ]