# -*- coding: utf-8 -*-
# Copyright (C) 2016-TODAY touch:n:track <https://tnt.pythonanywhere.com>
# Part of tnt: BOM Product addon for Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "tnt: BOM Product",

    'summary': """
Auto Create BOM Product
    """,

    'description': """
Auto Create Products from Purchase Product BOM
    """,

    'author': "touch:n:track",
    'website': "https://tnt.pythonanywhere.com/",
    'category': 'Operations/Purchase',
    'version': '0.1',

    'depends': [
        'mrp',
        'purchase',
    ],

    'data': [
        'views/stock_picking_views.xml',
    ],

    'installable': True,
    'auto_install': False,
}
