# Generated by Django 5.0 on 2024-01-10 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='lasttname',
        ),
    ]
