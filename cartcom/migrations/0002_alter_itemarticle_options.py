# Generated by Django 4.2.6 on 2023-12-05 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartcom', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemarticle',
            options={'ordering': ('-created_at',), 'verbose_name': 'ItemArticle'},
        ),
    ]