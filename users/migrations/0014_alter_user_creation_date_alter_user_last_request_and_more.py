# Generated by Django 4.2.3 on 2023-08-09 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_user_creation_date_alter_user_last_request_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 12, 40, 28, 452506, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_request',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 12, 40, 28, 452535, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 12, 40, 28, 452527, tzinfo=datetime.timezone.utc)),
        ),
    ]
