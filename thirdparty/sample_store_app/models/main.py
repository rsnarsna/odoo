# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SampleStoreItem(models.Model):
    _name = 'sample.store.item'
    _description = 'Sample Store App Extension'

    name = fields.Char(string="Item Title", required=True)
    code = fields.Char(string="Store SKU Code", default="SKU-STORE-001")
    description = fields.Text(string="Extension Notes")
    active = fields.Boolean(string="Active in Store", default=True)

