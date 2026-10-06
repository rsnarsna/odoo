# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MarketingAutomationFlow(models.Model):
    _name = 'marketing.automation.flow'
    _description = 'Marketing Automation Engine'

    name = fields.Char(string="Campaign Flow Name", required=True)
    trigger_type = fields.Selection([
        ('lead_created', 'New Lead Added in CRM'),
        ('sale_confirmed', 'First Order Completed'),
        ('survey_submitted', 'Satisfaction Survey Filled'),
        ('cart_abandoned', 'Abandoned Web Cart')
    ], string="Trigger Event", default='lead_created', required=True)
    delay_hours = fields.Integer(string="Execution Delay (Hours)", default=24)
    total_enrolled = fields.Integer(string="Enrolled Contacts", default=0)
    state = fields.Selection([('draft', 'Draft'), ('running', 'Running Active'), ('paused', 'Paused')], default='draft')
    email_template = fields.Text(string="Automated Message Body")

    def action_start(self):
        for rec in self:
            rec.state = 'running'

    def action_pause(self):
        for rec in self:
            rec.state = 'paused'

