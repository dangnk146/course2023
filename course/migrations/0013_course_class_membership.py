# Generated by Django 4.2.5 on 2023-10-12 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_studentuser_isactive_teacheruser_isactive'),
        ('course', '0012_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='class_membership',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.classmembership'),
            preserve_default=False,
        ),
    ]