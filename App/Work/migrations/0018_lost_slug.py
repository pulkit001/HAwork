# Generated by Django 3.2.5 on 2021-08-25 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0017_auto_20210825_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='lost',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
