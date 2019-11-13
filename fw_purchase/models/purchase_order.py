# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    forecast_text = fields.Char(string='Forecast text', oldname='x_forecast_text')

    def purchase_uom_round_up(self):
        for obj in self:
            for l in obj.order_line:
                if l.product_qty % 1 > 0:
                    old_qty = l.product_qty
                    new_qty = int(old_qty) + (old_qty % 1 > 0)
                    l.write({'product_qty': new_qty, 'calculated_qty': old_qty})
                if l.price_unit == l.product_id.standard_price or l.price_unit == 0:
                    l.write({'price_unit': l.product_id.standard_price * l.product_id.uom_po_id.factor_inv})


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    calculated_qty = fields.Float(string='Calculated Quantity', oldname='x_calculated_qty')

