# -*- coding: utf-8 -*-
{
    'name': 'Recurring Subscriptions Engine',
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'summary': 'Recurring billing plans, automated renewals, MRR metrics and customer subscriptions',
    'description': """
        Recurring Subscriptions Engine - Fully runnable open-source thirdparty app store package.
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
