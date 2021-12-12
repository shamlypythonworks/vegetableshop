# Generated by Django 3.2.5 on 2021-11-17 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_prdttable'),
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quan', models.IntegerField()),
                ('listkee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartapp.cartlist')),
                ('prokee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.prdttable')),
            ],
        ),
    ]