# Generated by Django 4.1.4 on 2022-12-26 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile1',
            name='email',
        ),
    ]
