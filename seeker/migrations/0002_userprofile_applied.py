# Generated by Django 3.2.4 on 2023-08-08 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='applied',
            field=models.PositiveIntegerField(default=0),
        ),
    ]