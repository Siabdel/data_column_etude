# Generated by Django 4.2.6 on 2023-12-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copro', '0048_remove_lignedecandidature_agence_local_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lignedecandidature',
            name='provison_investissement',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
