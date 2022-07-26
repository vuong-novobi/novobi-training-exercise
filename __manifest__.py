# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Purchase Order Enhancement',
    'version' : '1.0',
    'summary': 'Advanced features of Purchase Order',
    'sequence': 10,
    'description': """
        Advanced features of Purchase Order
    """,
    'website': 'https://www.odoo.com/app',
    'images' : [],
    'depends' : ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'data/purchase_order_enhancement_data.xml',
        'wizard/archive_old_order_view.xml',
        'report/purchase_order_enhancement_report.xml',
        'views/purchase_order_enhancement_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [],
    'assets': {
        'web.assets_backend': [
            'purchase_order_enhancement/static/src/js/phone_number_widget.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
