# Generated by Django 3.1 on 2020-08-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_worker_image_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='image_profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
