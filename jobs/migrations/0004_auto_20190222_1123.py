# Generated by Django 2.1.5 on 2019-02-22 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='summary',
            new_name='body',
        ),
    ]