# Generated by Django 3.2.6 on 2022-10-25 11:15

import apps.home.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_postdocument_postmusic_postvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Название канала'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100, null=True, validators=[apps.home.validators.validate_post_name], verbose_name='Заголовок поста'),
        ),
    ]
