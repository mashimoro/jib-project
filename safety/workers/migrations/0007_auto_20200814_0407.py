# Generated by Django 3.1 on 2020-08-14 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0006_auto_20200814_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='primary_phone',
            field=models.TextField(max_length=10),
        ),
    ]
