# -*- coding: utf-8 -*-
{
    'name': 'Website Comment',
    'category': 'Website',
    'version': '9.0.1.0.0',
    'summary': 'This module adds a comment on website checkout.',
    'website': 'http://www.aktivsoftware.com',
    'author': 'Aktiv Software',
    'license': 'AGPL-3',
    'description': 'The purpose of this module is, it helps to add a comment box\
    on the website checkout and by confirming details it will gets saved too.',
    'depends': ['base', 'website_sale'],
    'data': [
        'views/sale_order_inherit_view.xml',
        'static/src/xml/website_sale_order_template.xml',
        'report/sale_report_template_inherited.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'auto_install': False,
    'installable': True,
    'application': False,
}
