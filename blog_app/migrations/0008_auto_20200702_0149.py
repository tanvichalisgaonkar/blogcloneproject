# Generated by Django 3.0.7 on 2020-07-01 20:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_auto_20200702_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 20, 19, 13, 233389, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 20, 19, 13, 231427, tzinfo=utc)),
        ),
    ]
