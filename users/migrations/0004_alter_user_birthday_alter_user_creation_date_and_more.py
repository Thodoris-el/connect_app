# Generated by Django 4.2.3 on 2023-08-08 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_birthday_alter_user_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 8, 12, 16, 46, 899412, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_request',
            field=models.DateField(default=datetime.datetime(2023, 8, 8, 12, 16, 46, 899487, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 8, 12, 16, 46, 899464, tzinfo=datetime.timezone.utc)),
        ),
    ]
