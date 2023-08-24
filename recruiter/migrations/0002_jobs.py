# Generated by Django 3.2.4 on 2023-08-07 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobnames', models.CharField(max_length=100)),
                ('dobss', models.DateField()),
                ('dobes', models.DateField()),
                ('exps', models.CharField(max_length=100)),
                ('places', models.CharField(max_length=100)),
                ('typs', models.CharField(choices=[('p', 'Part Time'), ('f', 'Full Time'), ('i', 'Internship')], default='default_typ', max_length=16)),
                ('sectors', models.CharField(max_length=100)),
                ('openingss', models.CharField(max_length=100)),
                ('creteria1s', models.CharField(max_length=100)),
                ('creteria2s', models.CharField(max_length=100)),
                ('creteria3s', models.CharField(max_length=100)),
                ('abouts', models.CharField(max_length=1000)),
            ],
        ),
    ]