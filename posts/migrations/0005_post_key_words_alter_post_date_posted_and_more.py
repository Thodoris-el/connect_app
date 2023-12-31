# Generated by Django 4.2.3 on 2023-08-09 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_is_active_alter_post_date_posted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='key_words',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 12, 40, 28, 474868, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 12, 40, 28, 474885, tzinfo=datetime.timezone.utc)),
        ),
    ]
