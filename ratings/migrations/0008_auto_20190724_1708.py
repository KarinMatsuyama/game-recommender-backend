# Generated by Django 2.2.2 on 2019-07-24 17:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0007_auto_20190723_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 17, 8, 49, 608588, tzinfo=utc)),
        ),
    ]
