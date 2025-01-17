# Generated by Django 5.1.2 on 2024-11-14 20:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0004_user_delete_automobile_author_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, default=None
            ),
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
