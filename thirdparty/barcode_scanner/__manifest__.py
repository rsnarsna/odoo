# -*- coding: utf-8 -*-
{
    'name': 'Barcode Scanner Mobile Interface',
    'version': '19.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Handheld wireless barcode scanner session manager for warehouse operations',
    'description': """
        Barcode Scanner Mobile Interface - Fully runnable open-source thirdparty app store package.
        Replaces proprietary Enterprise features with community-maintained models and views.
    """,
    'author': 'Odoo Open Source Community',
    'license': 'LGPL-3',
    'depends': ['base', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
