# Generated by Django 3.1.2 on 2020-10-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20201008_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrating',
            name='feedback',
            field=models.CharField(max_length=2000),
        ),
    ]
