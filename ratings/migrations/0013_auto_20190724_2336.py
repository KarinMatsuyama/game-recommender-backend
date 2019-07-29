# Generated by Django 2.2.2 on 2019-07-24 23:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0012_auto_20190724_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='igdb_id',
            new_name='igdbid',
        ),
        migrations.AlterField(
            model_name='rating',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 23, 36, 24, 724652, tzinfo=utc)),
        ),
    ]
