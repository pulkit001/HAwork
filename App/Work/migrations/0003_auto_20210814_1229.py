# Generated by Django 3.2.5 on 2021-08-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]