# Generated by Django 4.2.5 on 2023-12-04 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='danhmuctag',
            name='course',
        ),
        migrations.DeleteModel(
            name='ChuongTag',
        ),
        migrations.DeleteModel(
            name='DanhMucTag',
        ),
    ]