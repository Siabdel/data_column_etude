# Generated by Django 4.2.6 on 2023-10-25 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('copro', '0003_remove_residence_photo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piece',
            old_name='photos',
            new_name='pieces',
        ),
    ]
