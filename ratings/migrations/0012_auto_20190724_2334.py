# Generated by Django 2.2.2 on 2019-07-24 23:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0011_auto_20190724_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 23, 34, 18, 597288, tzinfo=utc)),
        ),
    ]
