# Generated by Django 2.2.4 on 2020-10-12 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0021_auto_20201007_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingdate',
            name='last_modified',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 10, 12, 8, 25, 7, 75237)),
        ),
    ]
