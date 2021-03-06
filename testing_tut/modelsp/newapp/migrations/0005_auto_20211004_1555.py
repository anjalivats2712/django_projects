# Generated by Django 2.1.5 on 2021-10-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_empinfo_working_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='empinfo',
            name='job',
        ),
        migrations.AddField(
            model_name='empinfo',
            name='emp_job',
            field=models.ManyToManyField(blank=True, to='newapp.AvailableJob'),
        ),
    ]
