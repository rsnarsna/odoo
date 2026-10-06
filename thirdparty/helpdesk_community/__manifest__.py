# -*- coding: utf-8 -*-
{
    'name': 'Community Support Ticket Desk',
    'version': '19.0.1.0.0',
    'category': 'Services/Helpdesk',
    'summary': 'Customer issue management, ticket priority dispatching, and resolution SLAs',
    'description': """
        Community Support Ticket Desk - Fully runnable open-source thirdparty app store package.
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
