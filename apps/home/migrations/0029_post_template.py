# Generated by Django 3.2.6 on 2022-11-12 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20221112_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.template', verbose_name='Шаблон'),
        ),
    ]
