# Generated by Django 4.2.6 on 2023-10-28 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('copro', '0015_remove_etude_type_presta'),
    ]

    operations = [
        migrations.AddField(
            model_name='etude',
            name='type_presta',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='copro.prestationservice'),
            preserve_default=False,
        ),
    ]
