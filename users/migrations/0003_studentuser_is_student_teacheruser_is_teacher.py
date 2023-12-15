# Generated by Django 4.2.5 on 2023-10-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_studentuser_isactive_teacheruser_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='teacheruser',
            name='is_teacher',
            field=models.BooleanField(default=True),
        ),
    ]
