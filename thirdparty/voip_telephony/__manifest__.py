# -*- coding: utf-8 -*-
{
    'name': 'VoIP SIP Call Manager',
    'version': '19.0.1.0.0',
    'category': 'Productivity/VoIP',
    'summary': 'In-browser WebRTC softphone dialer, Asterisk/FreePBX bridge, and call history logs',
    'description': """
        VoIP SIP Call Manager - Fully runnable open-source thirdparty app store package.
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
