# Generated by Django 4.2.5 on 2023-12-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0027_remove_chuongtag_danhmuctag_delete_danhmuctag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chuongtag',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
