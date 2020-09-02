# -*- coding: utf-8 -*-
# Copyright (C) 2016-TODAY touch:n:track <https://tnt.pythonanywhere.com>
# Part of tnt: BOM Product addon for Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, SUPERUSER_ID, _


class Picking(models.Model):
    _inherit = 'stock.picking'

    def button_validate_bom(self):
        self.ensure_one()
        self.button_validate()
        products = [{
            'product_id': move_line.product_id,
            'name': move_line.product_id.name,
            'lot_name': move_line.lot_name,
        } for move_line in self.move_line_ids if move_line.lot_name]

        for product in products:
            product_id = product.get('product_id')
            if product_id:
                for bom in product_id.bom_ids[:1]:
                    for i, bom_line in enumerate(bom.bom_line_ids):
                        bom_line.product_id.sudo().copy({
                            'name': '{} ({}#{:02d})'.format(bom_line.product_id.name, product.get('lot_name'), i + 1),
                            'default_code': bom_line.product_id.default_code,
                        })

        return
