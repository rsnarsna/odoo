# -*- coding: utf-8 -*-
{
    'name': 'Community Documents Workspace',
    'version': '19.0.1.0.0',
    'category': 'Document Management',
    'summary': 'Enterprise document folders, cloud vaults, tags, and file attachments',
    'description': """
        Community Documents Workspace - Fully runnable open-source thirdparty app store package.
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
