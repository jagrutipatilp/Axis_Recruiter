# Generated by Django 3.2.4 on 2023-08-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0002_userprofile_applied'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRProfile',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='passw',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
