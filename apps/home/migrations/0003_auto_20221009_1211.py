# Generated by Django 3.2.6 on 2022-10-09 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20221009_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='button',
            name='user',
        ),
        migrations.AddField(
            model_name='chat',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
