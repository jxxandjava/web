# Generated by Django 2.1.7 on 2019-03-26 17:59

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_auto_20190325_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='HackathonEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('logo_svg', models.FileField(blank=True, upload_to='')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bounty',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bounties', to='dashboard.HackathonEvent'),
        ),
    ]