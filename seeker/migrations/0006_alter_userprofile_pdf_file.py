# Generated by Django 3.2.4 on 2023-08-10 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0005_userprofile_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]
