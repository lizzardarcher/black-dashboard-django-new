# Generated by Django 3.2.6 on 2022-11-12 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0025_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='post',
        ),
        migrations.AddField(
            model_name='template',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
