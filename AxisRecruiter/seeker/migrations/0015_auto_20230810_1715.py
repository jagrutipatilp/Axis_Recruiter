# Generated by Django 3.2.4 on 2023-08-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0014_auto_20230810_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='resume',
            field=models.FileField(blank=True, default='', max_length=1048570, null=True, upload_to='resumes/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='resumetxt',
            field=models.CharField(default='', max_length=1048570),
        ),
    ]
