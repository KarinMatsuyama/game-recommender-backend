# Generated by Django 2.2.2 on 2019-07-25 20:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0015_auto_20190725_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 25, 20, 7, 6, 973202, tzinfo=utc)),
        ),
    ]