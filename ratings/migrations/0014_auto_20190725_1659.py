# Generated by Django 2.2.2 on 2019-07-25 16:59

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ratings', '0013_auto_20190724_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 25, 16, 59, 3, 388424, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]