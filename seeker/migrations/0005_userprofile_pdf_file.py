# Generated by Django 3.2.4 on 2023-08-10 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0004_auto_20230808_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pdf_file',
            field=models.FileField(default=None, upload_to='pdfs/'),
        ),
    ]
