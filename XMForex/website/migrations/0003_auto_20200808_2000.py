# Generated by Django 2.1.5 on 2020-08-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200808_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='imagefile',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='img'),
        ),
    ]