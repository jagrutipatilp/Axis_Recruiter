# Generated by Django 3.2.4 on 2023-08-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0022_userprofile_resumetxt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='resumetxt',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='txteresum',
            field=models.TextField(default=''),
        ),
    ]
