# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StudioLowcodeField(models.Model):
    _name = 'studio.lowcode.field'
    _description = 'Community Studio Low-Code Builder'

    name = fields.Char(string="Technical Field Name", required=True)
    label = fields.Char(string="User-facing Label", required=True)
    model_id = fields.Many2one('ir.model', string="Target Odoo Model", required=True, ondelete='cascade')
    field_type = fields.Selection([
        ('char', 'Text Line (Char)'),
        ('text', 'Multi-line Text'),
        ('integer', 'Integer Number'),
        ('float', 'Currency / Decimal Float'),
        ('boolean', 'Yes / No Toggle'),
        ('date', 'Date Picker'),
        ('datetime', 'Date & Time Picker')
    ], string="Data Type", default='char', required=True)
    is_required = fields.Boolean(string="Required Field", default=False)
    state = fields.Selection([('draft', 'Draft Definition'), ('active', 'Active on Views')], default='draft')
    notes = fields.Text(string="Field Purpose")

    def action_activate(self):
        for rec in self:
            rec.state = 'active'

