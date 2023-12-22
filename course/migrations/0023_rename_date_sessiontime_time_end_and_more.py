# Generated by Django 4.2.5 on 2023-10-16 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_classmembership_alter_course_class_membership_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sessiontime',
            old_name='date',
            new_name='time_end',
        ),
        migrations.RenameField(
            model_name='sessiontime',
            old_name='time',
            new_name='time_start',
        ),
        migrations.CreateModel(
            name='SessionTimeLessionExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lessionexam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.lessionexam')),
                ('sessiontime', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.sessiontime')),
            ],
        ),
    ]