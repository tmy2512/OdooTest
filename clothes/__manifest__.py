# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Clothes',
    'version' : '1.2',
    'summary': 'test',
    'sequence': 10,
    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'depends': ['account'],

    'data': [
        # 'security/ir.model.access.csv',
        # 'security/estate_property_security.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'assets': {

    },
    'license': 'LGPL-3',
}
