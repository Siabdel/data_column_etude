# Generated by Django 4.2.6 on 2023-10-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copro', '0020_remove_lignedecandidature_site_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='lignedecandidature',
            name='site_web',
            field=models.URLField(blank=True, null=True),
        ),
    ]
