# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170922_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subsubcategory',
            field=models.ForeignKey(related_name='products', default=0, blank=True, to='shop.SubSubCategory'),
        ),
    ]
