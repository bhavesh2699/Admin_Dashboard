# Generated by Django 2.2.5 on 2019-12-25 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191225_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='b',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='c',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='d',
        ),
    ]
