# Generated by Django 4.1.4 on 2023-04-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0004_projectassignment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectassignment',
            name='status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
