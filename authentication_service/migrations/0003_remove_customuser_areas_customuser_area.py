# Generated by Django 4.1.7 on 2023-09-12 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_service', '0002_remove_customuser_area_customuser_areas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='areas',
        ),
        migrations.AddField(
            model_name='customuser',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='authentication_service.area'),
        ),
    ]
