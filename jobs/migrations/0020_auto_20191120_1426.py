# Generated by Django 2.1.5 on 2019-11-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_auto_20191015_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='url_slug',
            field=models.SlugField(unique=True),
        ),
        migrations.RenameField(
            model_name='jobimage',
            old_name='job',
            new_name='job_linked',
        ),
    ]
