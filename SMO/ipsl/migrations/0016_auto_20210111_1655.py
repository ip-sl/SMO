# Generated by Django 3.1.5 on 2021-01-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipsl', '0015_auto_20210111_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screening',
            name='DOB',
            field=models.CharField(max_length=100, verbose_name='Date Of Birth'),
        ),
    ]
