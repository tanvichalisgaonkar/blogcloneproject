# Generated by Django 3.0.7 on 2020-07-01 13:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_auto_20200701_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 13, 26, 2, 374365, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 13, 26, 2, 374365, tzinfo=utc)),
        ),
    ]
