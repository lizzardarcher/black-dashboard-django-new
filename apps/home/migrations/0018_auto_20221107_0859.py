# Generated by Django 3.2.6 on 2022-11-07 08:59

import apps.home.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20221106_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='btn_name',
            new_name='btn_name_1',
        ),
        migrations.AddField(
            model_name='post',
            name='btn_name_2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='post',
            name='btn_name_3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='post',
            name='btn_name_4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True, validators=[apps.home.validators.post_ref_validator], verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url_text',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Текст внутри ссылки'),
        ),
    ]
