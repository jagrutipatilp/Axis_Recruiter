# Generated by Django 3.2.4 on 2023-08-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0019_remove_userprofile_resumetxt'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='resumetxt',
            field=models.CharField(default='', max_length=1),
        ),
    ]
