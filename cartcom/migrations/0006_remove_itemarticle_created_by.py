# Generated by Django 4.2.6 on 2023-12-07 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartcom', '0005_itemraw_alter_cartof_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemarticle',
            name='created_by',
        ),
    ]
