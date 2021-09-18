# Generated by Django 3.2.7 on 2021-09-16 02:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeathersFightApp', '0012_auto_20210916_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationrequest',
            name='request_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 2, 6, 6, 866412)),
        ),
        migrations.AlterField(
            model_name='deleterequest',
            name='delete_request_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 2, 6, 6, 867060)),
        ),
        migrations.AlterField(
            model_name='editrequest',
            name='edit_request_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 2, 6, 6, 866752)),
        ),
    ]
