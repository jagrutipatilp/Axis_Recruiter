# Generated by Django 3.2.4 on 2023-08-07 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0003_delete_jobs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='Jobs',
        ),
    ]
