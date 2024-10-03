from odoo import models, fields

class TestModel(models.Model):
    _name = 'test.model'

    name = fields.Char(string='Name')


class AccountAccountTag(models.Model):
    _inherit = 'account.account.tag'


