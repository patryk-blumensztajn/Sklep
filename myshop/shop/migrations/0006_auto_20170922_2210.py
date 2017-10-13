# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20170922_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subsubcategory',
            field=models.ForeignKey(related_name='products', blank=True, to='shop.SubSubCategory'),
        ),
    ]
