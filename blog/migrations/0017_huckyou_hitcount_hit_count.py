# Generated by Django 2.0.13 on 2021-10-29 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200816_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='huckyou',
            name='hitcount_hit_count',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]