# Generated by Django 2.1.3 on 2018-11-09 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20181109_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todu',
            name='status',
            field=models.CharField(max_length=3),
        ),
    ]