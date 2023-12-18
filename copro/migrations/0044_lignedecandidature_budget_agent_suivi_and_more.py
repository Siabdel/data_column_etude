# Generated by Django 4.2.6 on 2023-12-18 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copro', '0043_pjevent_created_pjevent_created_by_pjevent_modified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lignedecandidature',
            name='budget_agent_suivi',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lignedecandidature',
            name='budget_maintenance',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lignedecandidature',
            name='budget_menage',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lignedecandidature',
            name='budget_picine',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lignedecandidature',
            name='proposition_transition',
            field=models.BooleanField(default=False, verbose_name='proposition transition'),
        ),
        migrations.AddField(
            model_name='lignedecandidature',
            name='propostion_recouverement',
            field=models.BooleanField(default=False, verbose_name='Proposition de recouverement '),
        ),
        migrations.AddField(
            model_name='lignedecandidature',
            name='reponse_questionnaire',
            field=models.BooleanField(default=False, verbose_name='reponse au questionnaire '),
        ),
    ]