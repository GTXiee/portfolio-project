# Generated by Django 2.1.5 on 2019-11-29 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0020_auto_20191120_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobimage',
            name='is_thumbnail',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='jobimage',
            name='order',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='jobimage',
            unique_together={('job_linked', 'is_thumbnail'), ('job_linked', 'order')},
        ),
    ]
