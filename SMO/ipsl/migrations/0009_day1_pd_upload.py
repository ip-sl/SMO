# Generated by Django 3.1.5 on 2021-01-05 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipsl', '0008_auto_20210105_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='day1',
            name='PD_Upload',
            field=models.FileField(help_text='If <b>Yes</b> Upload file', null=True, upload_to='', verbose_name='Protocol Deviation Upload'),
        ),
    ]
