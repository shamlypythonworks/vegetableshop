# Generated by Django 3.2.5 on 2021-11-18 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_auto_20211117_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categtable',
            options={'ordering': ('ctname',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
