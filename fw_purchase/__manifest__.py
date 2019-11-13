# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'fw_purchase',
    'version': '0.1',
    'website': 'https://www.odoo.com/',
    'category': 'fw',
    'sequence': 10,
    'summary': 'Feuerwear purchase customizations',
    'depends': [
        'purchase',
    ],
    'description': """
    Round up proposed qties on the PO to the next highest Purchase-UOM. 
    Create "Forecast PO's" to inform the supplier of the yearly forecased qty: if the field "forecast_text" is set, then the PO-Report takes this text as referece (instead of POxxxx).
    """,
    'data': [
        'views/purchase_order_views.xml',
        'report/purchase_report_templates.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
