# Generated by Django 3.2.5 on 2021-12-09 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0005_alter_categtable_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlisttable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wishkee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.prdttable')),
            ],
        ),
    ]
