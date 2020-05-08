# -*- coding: utf-8 -*-
{
    'name': "dni_password",

    'summary': """
         Use DNI like portal user password""",

    'description': """
        Use DNI (Documento Nacional de Identidad, Argentina) like portal user password
    """,

    'author': "Moldeo Interactive",
    'website': "http://www.moldeointeractive.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
