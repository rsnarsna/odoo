# -*- coding: utf-8 -*-
{
    'name': 'Community Studio Low-Code Builder',
    'version': '19.0.1.0.0',
    'category': 'Customization',
    'summary': 'Low-code custom fields, model extensions, and form designer without coding',
    'description': """
        Community Studio Low-Code Builder - Fully runnable open-source thirdparty app store package.
        Replaces proprietary Enterprise features with community-maintained models and views.
    """,
    'author': 'Odoo Open Source Community',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
