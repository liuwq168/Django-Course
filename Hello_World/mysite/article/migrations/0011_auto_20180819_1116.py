# Generated by Django 2.0.5 on 2018-08-19 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20180819_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='readed_num',
            field=models.IntegerField(default=0),
        ),
    ]