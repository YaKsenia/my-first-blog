# Generated by Django 2.0.13 on 2020-01-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200130_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='MEDIA_URL'),
        ),
    ]