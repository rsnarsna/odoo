# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PayrollWageStructure(models.Model):
    _name = 'payroll.wage.structure'
    _description = 'Community Payroll & Wage Desk'

    name = fields.Char(string="Salary Structure Code", required=True)
    employee_id = fields.Many2one('hr.employee', string="Employee")
    basic_wage = fields.Float(string="Basic Wage ($)", required=True, default=3500.0)
    housing_allowance = fields.Float(string="Housing Allowance ($)", default=500.0)
    transport_allowance = fields.Float(string="Transport Allowance ($)", default=250.0)
    tax_rate_pct = fields.Float(string="Tax Deduction (%)", default=12.0)
    net_payable = fields.Float(string="Net Estimated Pay ($)", compute="_compute_net", store=True)

    @api.depends('basic_wage', 'housing_allowance', 'transport_allowance', 'tax_rate_pct')
    def _compute_net(self):
        for rec in self:
            gross = rec.basic_wage + rec.housing_allowance + rec.transport_allowance
            deductions = gross * (rec.tax_rate_pct / 100.0)
            rec.net_payable = gross - deductions

