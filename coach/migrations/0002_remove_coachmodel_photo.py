# Generated by Django 4.2.5 on 2023-09-10 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coachmodel',
            name='photo',
        ),
    ]