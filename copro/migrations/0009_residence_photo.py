# Generated by Django 4.2.6 on 2023-10-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copro', '0008_rename_documents_pjointe_piece'),
    ]

    operations = [
        migrations.AddField(
            model_name='residence',
            name='photo',
            field=models.ImageField(default=None, upload_to='upload/'),
            preserve_default=False,
        ),
    ]
