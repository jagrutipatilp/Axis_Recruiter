# Generated by Django 3.2.4 on 2023-08-10 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0018_alter_userprofile_resumetxt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='resumetxt',
        ),
    ]