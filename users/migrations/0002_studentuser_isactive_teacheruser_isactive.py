# Generated by Django 4.2.5 on 2023-10-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacheruser',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]
