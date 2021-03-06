# Generated by Django 3.2.5 on 2021-11-17 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_prdttable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categtable',
            name='ctname',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='categtable',
            name='slug',
            field=models.SlugField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
