# Generated by Django 3.2.5 on 2021-12-09 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0007_auto_20211208_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlisttable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prowishkee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.prdttable')),
                ('wshlist_kee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.wish_list')),
            ],
        ),
    ]
