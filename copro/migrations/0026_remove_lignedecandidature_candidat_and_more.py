# Generated by Django 4.2.6 on 2023-11-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copro', '0025_category_contacte_documentjoint_evenement_gdocument_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lignedecandidature',
            name='candidat',
        ),
        migrations.AddField(
            model_name='lignedecandidature',
            name='offre_recu',
            field=models.BooleanField(default=False, verbose_name='Candidat a fait une offre'),
        ),
    ]
