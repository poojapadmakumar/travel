# Generated by Django 3.2.16 on 2022-12-14 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_place2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place2',
            old_name='desc',
            new_name='desc2',
        ),
    ]
