# Generated by Django 4.2.6 on 2023-10-26 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('copro', '0006_residence_color_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pjointe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('documents', models.FileField(upload_to='upload/')),
                ('candidature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copro.lignedecandidature')),
            ],
        ),
    ]
