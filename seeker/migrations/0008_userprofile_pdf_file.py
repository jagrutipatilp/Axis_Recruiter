# Generated by Django 3.2.4 on 2023-08-10 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0007_remove_userprofile_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pdf_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
