# Generated by Django 3.0.7 on 2020-07-02 11:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0010_auto_20200702_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 11, 26, 15, 487061, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 11, 26, 15, 486065, tzinfo=utc)),
        ),
    ]
