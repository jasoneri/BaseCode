# Generated by Django 2.2 on 2019-04-26 03:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(default=datetime.datetime(2019, 4, 26, 3, 57, 47, 930190, tzinfo=utc))),
                ('update_time', models.DateTimeField(default=datetime.datetime(2019, 4, 26, 3, 57, 47, 930190, tzinfo=utc))),
                ('datastatus', models.SmallIntegerField(default=0)),
            ],
        ),
    ]
