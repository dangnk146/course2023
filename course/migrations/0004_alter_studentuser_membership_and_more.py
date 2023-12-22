# Generated by Django 4.2.5 on 2023-10-11 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_remove_teacheruser_membership_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='membership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.classmembership'),
        ),
        migrations.AlterField(
            model_name='teacheruser',
            name='memberships',
            field=models.ManyToManyField(null=True, to='course.classmembership'),
        ),
    ]