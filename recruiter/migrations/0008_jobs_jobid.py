# Generated by Django 3.2.4 on 2023-08-08 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0007_delete_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='jobid',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
