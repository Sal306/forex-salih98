# Generated by Django 2.1.5 on 2020-08-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200808_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='imagefile',
            field=models.FileField(null=True, upload_to='images/', verbose_name='img'),
        ),
    ]