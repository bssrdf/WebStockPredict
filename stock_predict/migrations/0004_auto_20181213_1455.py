# Generated by Django 2.1.4 on 2018-12-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_predict', '0003_auto_20181212_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historydata',
            name='start_date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predictdata',
            name='start_date',
            field=models.CharField(max_length=30),
        ),
    ]
