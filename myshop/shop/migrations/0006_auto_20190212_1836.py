# Generated by Django 2.1.5 on 2019-02-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190212_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]