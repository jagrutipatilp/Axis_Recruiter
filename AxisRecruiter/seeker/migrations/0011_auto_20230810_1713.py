# Generated by Django 3.2.4 on 2023-08-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0010_alter_userprofile_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='resumetxt',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='resume',
            field=models.FileField(blank=True, default='', max_length=1000, null=True, upload_to='resumes/'),
        ),
    ]