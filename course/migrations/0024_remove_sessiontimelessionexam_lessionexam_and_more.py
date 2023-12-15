# Generated by Django 4.2.5 on 2023-10-16 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_rename_date_sessiontime_time_end_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessiontimelessionexam',
            name='lessionexam',
        ),
        migrations.RemoveField(
            model_name='sessiontimelessionexam',
            name='sessiontime',
        ),
        migrations.AddField(
            model_name='sessiontimelessionexam',
            name='timeend',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sessiontimelessionexam',
            name='timestart',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lessionexam',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.sessiontimelessionexam'),
        ),
        migrations.DeleteModel(
            name='SessionTime',
        ),
    ]
