# -*- coding: utf-8 -*-
{
    'name': 'Marketing Automation Engine',
    'version': '19.0.1.0.0',
    'category': 'Marketing',
    'summary': 'Automated email sequences, subscriber journeys, event triggers and lead nurturing',
    'description': """
        Marketing Automation Engine - Fully runnable open-source thirdparty app store package.
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
