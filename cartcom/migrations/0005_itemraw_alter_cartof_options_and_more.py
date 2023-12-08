# Generated by Django 4.2.6 on 2023-12-06 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cartcom', '0004_itemarticle_content_type_itemarticle_object_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemRaw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_message', models.JSONField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='cartof',
            options={'ordering': ('-created_at',), 'verbose_name': 'cart', 'verbose_name_plural': 'cartsOf'},
        ),
        migrations.AlterModelOptions(
            name='itemarticle',
            options={'ordering': ('-created_at',), 'verbose_name': 'ItemArticle', 'verbose_name_plural': 'ItemArticles'},
        ),
        migrations.RemoveField(
            model_name='cartof',
            name='creation_date',
        ),
        migrations.AlterField(
            model_name='cartof',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]