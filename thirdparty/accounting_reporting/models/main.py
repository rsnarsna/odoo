# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountingReportHub(models.Model):
    _name = 'accounting.report.hub'
    _description = 'Community Accounting Reports Hub'

    name = fields.Char(string="Report Title", required=True)
    report_type = fields.Selection([
        ('pnl', 'Profit and Loss Summary'),
        ('balance_sheet', 'Executive Balance Sheet'),
        ('cash_flow', 'Cash Flow Analysis'),
        ('aged_partner', 'Aged Receivables & Payables'),
        ('tax', 'Tax Audit Report')
    ], string="Report Type", default="pnl", required=True)
    date_from = fields.Date(string="From Date", default=fields.Date.context_today)
    date_to = fields.Date(string="To Date", default=fields.Date.context_today)
    total_debit = fields.Float(string="Total Debit", default=0.0)
    total_credit = fields.Float(string="Total Credit", default=0.0)
    net_margin = fields.Float(string="Net Margin / Balance", compute="_compute_margin", store=True)
    status = fields.Selection([('draft', 'Draft'), ('calculated', 'Calculated'), ('audited', 'Audited')], default='draft')
    notes = fields.Text(string="Financial Auditor Notes")

    @api.depends('total_debit', 'total_credit')
    def _compute_margin(self):
        for rec in self:
            rec.net_margin = rec.total_debit - rec.total_credit

    def action_calculate(self):
        for rec in self:
            rec.total_debit = 125000.00
            rec.total_credit = 84000.00
            rec.status = 'calculated'

