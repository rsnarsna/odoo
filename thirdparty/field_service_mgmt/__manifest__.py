# -*- coding: utf-8 -*-
{
    'name': 'Field Service Dispatch Hub',
    'version': '19.0.1.0.0',
    'category': 'Services',
    'summary': 'Technician job dispatch, customer site visits, GPS routing and work completion',
    'description': """
        Field Service Dispatch Hub - Fully runnable open-source thirdparty app store package.
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
