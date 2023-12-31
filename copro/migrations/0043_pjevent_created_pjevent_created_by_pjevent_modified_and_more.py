# Generated by Django 4.2.6 on 2023-12-08 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('copro', '0042_alter_lignedecandidature_comment_rating_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='pjevent',
            name='created',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
        migrations.AddField(
            model_name='pjevent',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pjevent',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Creation'),
        ),
        migrations.AlterField(
            model_name='document',
            name='created',
            field=models.DateField(auto_created=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='etude',
            name='created_at',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='etude',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='created',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='created on'),
        ),
        migrations.AlterField(
            model_name='gdocument',
            name='created',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lignedecandidature',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lignedecandidature',
            name='created_at',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='created',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='pjetude',
            name='created',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='pjointe',
            name='created',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='created on'),
        ),
    ]
