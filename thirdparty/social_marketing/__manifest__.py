# -*- coding: utf-8 -*-
{
    'name': 'Social Media Broadcast Hub',
    'version': '19.0.1.0.0',
    'category': 'Social',
    'summary': 'Multi-channel social post scheduler, analytics stream, and audience engagement',
    'description': """
        Social Media Broadcast Hub - Fully runnable open-source thirdparty app store package.
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
