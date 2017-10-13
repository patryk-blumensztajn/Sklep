# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20170922_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='shop.Product')),
                ('ram', models.DecimalField(verbose_name=b'Screen size', max_digits=4, decimal_places=2)),
            ],
            bases=('shop.product',),
        ),
    ]
