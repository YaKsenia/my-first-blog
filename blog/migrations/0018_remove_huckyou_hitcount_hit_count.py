# Generated by Django 2.0.13 on 2021-10-29 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_huckyou_hitcount_hit_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='huckyou',
            name='hitcount_hit_count',
        ),
    ]