# Generated by Django 3.0.7 on 2020-07-01 13:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20200701_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 13, 14, 15, 356125, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 13, 14, 15, 356125, tzinfo=utc)),
        ),
    ]
