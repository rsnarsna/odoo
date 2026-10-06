# -*- coding: utf-8 -*-
from odoo import models, fields, api

class BarcodeScannerSession(models.Model):
    _name = 'barcode.scanner.session'
    _description = 'Barcode Scanner Mobile Interface'

    name = fields.Char(string="Session Name", required=True, default=lambda self: "SCAN-" + fields.Date.today().strftime('%Y%m%d'))
    warehouse_id = fields.Many2one('stock.warehouse', string="Warehouse")
    operator_id = fields.Many2one('res.users', string="Scanner Operator", default=lambda self: self.env.user)
    last_barcode = fields.Char(string="Last Barcode Scanned")
    scan_count = fields.Integer(string="Total Scans", default=0)
    state = fields.Selection([('draft', 'Ready'), ('active', 'Scanning In Progress'), ('done', 'Session Closed')], default='draft')
    notes = fields.Text(string="Session Log")

    def action_start(self):
        for rec in self:
            rec.state = 'active'

    def action_close(self):
        for rec in self:
            rec.state = 'done'

