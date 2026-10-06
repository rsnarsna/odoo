# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FieldServiceCustomOrder(models.Model):
    _name = 'fieldservice.custom.order'
    _description = 'Field Service Dispatch Hub'

    name = fields.Char(string="Order Reference", required=True, default=lambda self: "FSO-" + fields.Date.today().strftime('%Y%m%d'))
    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    technician_id = fields.Many2one('res.users', string="Assigned Field Tech")
    scheduled_date = fields.Datetime(string="Scheduled Service Date", default=fields.Datetime.now)
    service_address = fields.Char(string="Site Address")
    state = fields.Selection([
        ('draft', 'New'),
        ('assigned', 'Dispatched'),
        ('in_progress', 'On Site Work'),
        ('completed', 'Done / Signed'),
        ('cancelled', 'Cancelled')
    ], string="Work Order Status", default='draft')
    work_summary = fields.Text(string="Work Completed Notes")

    def action_assign(self):
        for rec in self:
            rec.state = 'assigned'

    def action_start(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_complete(self):
        for rec in self:
            rec.state = 'completed'

