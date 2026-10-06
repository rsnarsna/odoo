# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HelpdeskSupportDesk(models.Model):
    _name = 'helpdesk.support.desk'
    _description = 'Community Support Ticket Desk'

    name = fields.Char(string="Ticket Subject", required=True)
    ticket_id = fields.Char(string="Ticket ID", default=lambda self: "TICK-" + fields.Date.today().strftime('%Y%m%d'))
    partner_id = fields.Many2one('res.partner', string="Customer")
    assigned_user_id = fields.Many2one('res.users', string="Assigned Support Agent", default=lambda self: self.env.user)
    priority = fields.Selection([('0', 'Low'), ('1', 'Normal'), ('2', 'High'), ('3', 'Urgent')], string="Priority", default='1')
    stage = fields.Selection([
        ('new', 'New Inquiry'),
        ('in_progress', 'Investigating'),
        ('waiting', 'Customer Pending'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
    ], string="Support Stage", default='new')
    description = fields.Text(string="Customer Issue Details")
    resolution_notes = fields.Text(string="Resolution & Root Cause")

    def action_resolve(self):
        for rec in self:
            rec.stage = 'resolved'

    def action_close(self):
        for rec in self:
            rec.stage = 'closed'

