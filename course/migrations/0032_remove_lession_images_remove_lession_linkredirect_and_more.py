# Generated by Django 4.2.5 on 2023-12-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0031_alter_chuongtag_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lession',
            name='images',
        ),
        migrations.RemoveField(
            model_name='lession',
            name='linkredirect',
        ),
        migrations.RemoveField(
            model_name='lession',
            name='linkvideo',
        ),
        migrations.RemoveField(
            model_name='lessionexam',
            name='images',
        ),
        migrations.RemoveField(
            model_name='lessionexam',
            name='linkredirect',
        ),
        migrations.RemoveField(
            model_name='lessionexam',
            name='linkvideo',
        ),
        migrations.AddField(
            model_name='lession',
            name='baigiangtuongtac',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lession',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lession',
            name='pptx',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lessionexam',
            name='baigiangtuongtac',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lessionexam',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lessionexam',
            name='pptx',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
