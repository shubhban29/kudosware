# Generated by Django 3.2.4 on 2021-06-06 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_auto_20210606_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
