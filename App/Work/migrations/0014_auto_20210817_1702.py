# Generated by Django 3.2.5 on 2021-08-17 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0013_remove_lost_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FoundList',
        ),
        migrations.DeleteModel(
            name='LostList',
        ),
    ]
