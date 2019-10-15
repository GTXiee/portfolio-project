# Generated by Django 2.1.5 on 2019-10-07 21:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_auto_20191007_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='technologies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('python', 'Python'), ('django', 'Django'), ('postgresql', 'PostgreSQL'), ('bootstrap', 'Bootstrap'), ('javascript', 'JavaScript')], max_length=50), null=True, size=None),
        ),
    ]
