# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SubscriptionRecurringPlan(models.Model):
    _name = 'subscription.recurring.plan'
    _description = 'Recurring Subscriptions Engine'

    name = fields.Char(string="Subscription Plan Title", required=True)
    partner_id = fields.Many2one('res.partner', string="Subscriber Customer", required=True)
    billing_period = fields.Selection([
        ('monthly', 'Monthly Recurring ($)'),
        ('quarterly', 'Quarterly Cycle ($)'),
        ('annual', 'Annual Contract ($)')
    ], string="Billing Interval", default='monthly', required=True)
    recurring_amount = fields.Float(string="Recurring Fee ($)", required=True, default=99.0)
    next_billing_date = fields.Date(string="Next Invoice Date", default=fields.Date.context_today)
    state = fields.Selection([
        ('draft', 'Quote'),
        ('active', 'Active Invoicing'),
        ('paused', 'Paused'),
        ('terminated', 'Cancelled')
    ], string="Subscription Status", default='draft')

    def action_activate(self):
        for rec in self:
            rec.state = 'active'

    def action_terminate(self):
        for rec in self:
            rec.state = 'terminated'

