# Generated by Django 4.0.3 on 2022-04-05 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0003_guestdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestdetails',
            name='reservation',
        ),
        migrations.AddField(
            model_name='guestdetails',
            name='reservation_id',
            field=models.IntegerField(default=1),
        ),
    ]
