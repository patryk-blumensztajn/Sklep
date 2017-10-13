# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_computer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('name',), 'verbose_name': 'subcategory', 'verbose_name_plural': 'subcategories'},
        ),
        migrations.AlterModelOptions(
            name='subsubcategory',
            options={'ordering': ('name',), 'verbose_name': 'subsubcategory', 'verbose_name_plural': 'subsubcategories'},
        ),
    ]
