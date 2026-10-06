# -*- coding: utf-8 -*-
{
    'name': 'Community Payroll & Wage Desk',
    'version': '19.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Employee wage structures, overtime rules, allowances, deductions, and payslip runs',
    'description': """
        Community Payroll & Wage Desk - Fully runnable open-source thirdparty app store package.
        Replaces proprietary Enterprise features with community-maintained models and views.
    """,
    'author': 'Odoo Open Source Community',
    'license': 'LGPL-3',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
