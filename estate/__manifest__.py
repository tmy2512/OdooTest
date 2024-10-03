# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Test Odoo',
    'version' : '1.2',
    'summary': 'Test & yeu My',
    'sequence': 10,
    'description': """""",
    'category': '',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['base','product', 'clothes'],
    'data': [
        'security/ir.model.access.csv',
        # 'security/estate_property_security.xml',
        'data/estate_property.csv',
        'views/product_views.xml',
        'views/estate_property_views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
    },
    'license': 'LGPL-3',
}
