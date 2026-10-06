# -*- coding: utf-8 -*-
from odoo import models, fields, api

class VoipCallRecord(models.Model):
    _name = 'voip.call.record'
    _description = 'VoIP SIP Call Manager'

    name = fields.Char(string="Call Subject", required=True)
    partner_id = fields.Many2one('res.partner', string="Caller / Contact")
    phone_number = fields.Char(string="Dialed Phone Number", required=True)
    call_direction = fields.Selection([('inbound', 'Inbound Call'), ('outbound', 'Outbound Dial')], default='outbound')
    call_duration_sec = fields.Integer(string="Duration (Seconds)", default=120)
    call_status = fields.Selection([('answered', 'Completed Call'), ('missed', 'Missed Call'), ('voicemail', 'Voicemail Left')], default='answered')
    call_notes = fields.Text(string="Call Summary & Notes")

