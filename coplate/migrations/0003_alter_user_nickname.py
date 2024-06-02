# Generated by Django 5.0.6 on 2024-06-02 11:45

import coplate.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coplate", "0002_user_nickname_alter_user_first_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="nickname",
            field=models.CharField(
                error_messages={"unique": "이미 사용중인 닉네임입니다."},
                max_length=15,
                null=True,
                unique=True,
                validators=[coplate.validators.validate_no_special_characters],
            ),
        ),
    ]
