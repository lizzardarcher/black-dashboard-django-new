# Generated by Django 3.2.6 on 2022-11-12 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_post_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatus',
            name='exp_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 12, 20, 55, 18, 332227), null=True, verbose_name='Оплачено по:'),
        ),
    ]