# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20170922_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(related_name='products', to='shop.SubCategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subsubcategory',
            field=models.ForeignKey(related_name='products', to='shop.SubSubCategory'),
        ),
    ]
