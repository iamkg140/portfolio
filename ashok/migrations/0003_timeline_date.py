# Generated by Django 3.2.8 on 2021-11-25 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashok', '0002_auto_20211124_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
