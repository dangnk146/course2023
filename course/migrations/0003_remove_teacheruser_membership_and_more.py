# Generated by Django 4.2.5 on 2023-10-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_studentuser_membership_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacheruser',
            name='membership',
        ),
        migrations.AddField(
            model_name='teacheruser',
            name='memberships',
            field=models.ManyToManyField(to='course.classmembership'),
        ),
    ]
