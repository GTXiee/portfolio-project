# Generated by Django 2.1.5 on 2019-10-06 20:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_job_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 10, 6, 20, 50, 7, 101993, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='jobimage',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job'),
        ),
    ]
