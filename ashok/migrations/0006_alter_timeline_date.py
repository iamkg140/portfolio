# Generated by Django 3.2.8 on 2021-11-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashok', '0005_rename_ashok_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='date',
            field=models.DateField(null=True),
        ),
    ]