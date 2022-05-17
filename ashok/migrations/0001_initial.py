# Generated by Django 3.2.8 on 2021-11-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ashok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=122, null=True)),
                ('post', models.CharField(max_length=122, null=True)),
                ('desc', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=122, null=True)),
                ('phone', models.CharField(max_length=122, null=True)),
                ('location', models.CharField(max_length=122, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=122)),
                ('post', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('title', models.CharField(max_length=122, null=True)),
                ('short_desc', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=122)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Social_links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=122, null=True)),
                ('twitter', models.CharField(max_length=122, null=True)),
                ('linkedin', models.CharField(max_length=122, null=True)),
                ('youtube', models.CharField(max_length=122, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('topic', models.CharField(max_length=122)),
                ('des', models.CharField(max_length=200)),
            ],
        ),
    ]
