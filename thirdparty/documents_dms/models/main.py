# -*- coding: utf-8 -*-
from odoo import models, fields, api

class DocumentsCustomWorkspace(models.Model):
    _name = 'documents.custom.workspace'
    _description = 'Community Documents Workspace'

    name = fields.Char(string="Folder / Workspace Name", required=True)
    code = fields.Char(string="Folder Code")
    description = fields.Text(string="Workspace Description")
    access_level = fields.Selection([
        ('public', 'All Internal Users'),
        ('restricted', 'Department Restricted'),
        ('private', 'Private Vault')
    ], string="Security Access", default="public", required=True)
    document_count = fields.Integer(string="Documents Count", default=0)
    owner_id = fields.Many2one('res.users', string="Folder Owner", default=lambda self: self.env.user)

