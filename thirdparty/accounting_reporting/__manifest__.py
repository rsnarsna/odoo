# -*- coding: utf-8 -*-
{
    'name': 'Community Accounting Reports Hub',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Dynamic P&L, Balance Sheet, Cash Flow and Executive Accounting Dashboards',
    'description': """
        Community Accounting Reports Hub - Fully runnable open-source thirdparty app store package.
        Replaces proprietary Enterprise features with community-maintained models and views.
    """,
    'author': 'Odoo Open Source Community',
    'license': 'LGPL-3',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
