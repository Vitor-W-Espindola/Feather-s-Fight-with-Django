# Generated by Django 3.2.7 on 2021-09-16 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeathersFightApp', '0018_auto_20210916_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deleterequest',
            name='delete_request_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 14, 40, 20, 664985)),
        ),
        migrations.AlterField(
            model_name='editrequest',
            name='edit_request_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 14, 40, 20, 664711)),
        ),
        migrations.AlterField(
            model_name='publicationrequest',
            name='request_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 14, 40, 20, 664413)),
        ),
    ]
