# Generated by Django 4.2.6 on 2023-10-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copro', '0005_rename_pieces_piece_piece'),
    ]

    operations = [
        migrations.AddField(
            model_name='residence',
            name='color_code',
            field=models.CharField(default='010101', max_length=6),
        ),
    ]