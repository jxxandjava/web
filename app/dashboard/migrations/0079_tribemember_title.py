# Generated by Django 2.2.4 on 2020-01-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0078_profile_as_representation'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribemember',
            name='title',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
