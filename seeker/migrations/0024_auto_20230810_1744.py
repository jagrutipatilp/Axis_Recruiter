# Generated by Django 3.2.4 on 2023-08-10 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0023_auto_20230810_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='about',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='ad1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='ad2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='applied',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='applied_jobs',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='edu',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gen',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='passw',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='per',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='pho1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='pho2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='post',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='uni',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='work',
        ),
    ]
