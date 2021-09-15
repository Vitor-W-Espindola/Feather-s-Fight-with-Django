# Generated by Django 3.2.7 on 2021-09-15 15:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FeathersFightApp', '0006_fight_await_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fight',
            name='await_request_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 15, 15, 1, 59, 348580)),
        ),
        migrations.CreateModel(
            name='DeleteRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='FeathersFightApp.fight')),
            ],
        ),
    ]