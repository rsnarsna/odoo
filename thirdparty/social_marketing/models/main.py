# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SocialBroadcastPost(models.Model):
    _name = 'social.broadcast.post'
    _description = 'Social Media Broadcast Hub'

    name = fields.Char(string="Post Headline", required=True)
    channel = fields.Selection([
        ('linkedin', 'LinkedIn Corporate'),
        ('twitter', 'X / Twitter'),
        ('facebook', 'Facebook Page'),
        ('instagram', 'Instagram Feed')
    ], string="Social Network", default='linkedin', required=True)
    message_content = fields.Text(string="Post Message", required=True)
    scheduled_datetime = fields.Datetime(string="Publish Schedule", default=fields.Datetime.now)
    state = fields.Selection([('draft', 'Draft'), ('scheduled', 'Scheduled'), ('published', 'Published')], default='draft')
    likes_count = fields.Integer(string="Likes & Reactions", default=0)
    comments_count = fields.Integer(string="Comments", default=0)

    def action_schedule(self):
        for rec in self:
            rec.state = 'scheduled'

    def action_publish_now(self):
        for rec in self:
            rec.state = 'published'

