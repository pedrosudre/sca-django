# Generated by Django 2.2.19 on 2022-12-20 15:05

import aplic.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0004_auto_20221027_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 260, 'width': 420}}, verbose_name='Imagem'),
        ),
    ]