# Generated by Django 2.1.5 on 2019-02-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, height_field=100, upload_to='products/%Y/%m/%d', width_field=100),
        ),
    ]
