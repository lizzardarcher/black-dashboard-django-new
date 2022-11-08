# Generated by Django 3.2.6 on 2022-11-08 20:19

import apps.home.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_chat_subscribers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='name',
        ),
        migrations.AddField(
            model_name='bot',
            name='ref',
            field=models.CharField(max_length=100, null=True, validators=[apps.home.validators.validate_post_name], verbose_name='Ссылка на бота'),
        ),
    ]
