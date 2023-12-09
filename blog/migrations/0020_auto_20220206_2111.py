# Generated by Django 2.0.13 on 2022-02-06 20:11

import blog.models
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20220124_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[1200, 800], upload_to=blog.models.get_image_filename),
        ),
    ]