# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SignatureDocumentVault(models.Model):
    _name = 'signature.document.vault'
    _description = 'Electronic Signatures Vault'

    name = fields.Char(string="Agreement Title", required=True)
    partner_id = fields.Many2one('res.partner', string="Signer Contact", required=True)
    signer_email = fields.Char(string="Signer Email", related="partner_id.email", readonly=False)
    state = fields.Selection([
        ('draft', 'Draft Agreement'),
        ('sent', 'Awaiting Signature'),
        ('signed', 'Legally Signed'),
        ('rejected', 'Declined')
    ], string="Signature Status", default='draft')
    audit_hash = fields.Char(string="Cryptographic Audit Hash")
    signed_date = fields.Datetime(string="Signed At")

    def action_send(self):
        for rec in self:
            rec.state = 'sent'

    def action_sign(self):
        for rec in self:
            rec.state = 'signed'
            rec.signed_date = fields.Datetime.now()
            rec.audit_hash = "SHA256:7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069"

