# -*- coding: utf-8 -*-
{
    'name': 'AI Smart Assistant',
    'version': '19.0.1.0.0',
    'category': 'Productivity',
    'summary': 'AI-powered prompt generator, copywriting assistant & SQL helper',
    'description': """
        AI Smart Assistant - Fully runnable open-source thirdparty app store package.
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
