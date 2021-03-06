# Generated by Django 2.2.2 on 2019-07-23 21:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_auto_20190722_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='genre',
            new_name='genres',
        ),
        migrations.AddField(
            model_name='game',
            name='igdb_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 23, 21, 14, 12, 220724, tzinfo=utc)),
        ),
    ]
