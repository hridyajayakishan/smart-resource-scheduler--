# Generated by Django 4.0.5 on 2023-02-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_alter_equipment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectassignment',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
