# Generated by Django 3.2.19 on 2023-06-03 19:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_alter_user_is_verified"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_verified",
        ),
    ]
