# Generated by Django 4.2.5 on 2023-10-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_studentuser_membership_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacheruser',
            name='memberships',
            field=models.ManyToManyField(blank=True, null=True, to='course.classmembership'),
        ),
    ]