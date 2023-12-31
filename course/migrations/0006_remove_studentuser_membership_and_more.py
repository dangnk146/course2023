# Generated by Django 4.2.5 on 2023-10-11 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_teacheruser_memberships'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='membership',
        ),
        migrations.RemoveField(
            model_name='teacheruser',
            name='memberships',
        ),
        migrations.CreateModel(
            name='MembershipTeacherUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.classmembership')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.teacheruser')),
            ],
        ),
        migrations.CreateModel(
            name='MembershipStudentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.classmembership')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.studentuser')),
            ],
        ),
    ]
