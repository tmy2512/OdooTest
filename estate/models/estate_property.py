from email.policy import default

from pkg_resources import require

from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate_property'
    _description = "real estate"

    name = fields.Char(string='Name Customer', index=True)
    description = fields.Text(default='Anh yeu my', readonly=True)
    postcode = fields.Char(default='21122003')
    date_availability = fields.Date(default=fields.Date.today, readonly=True)
    expected_price = fields.Float()
    selling_price = fields.Float(copy=False)
    bedrooms = fields.Integer(default=2)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Type is used to separate Norths and Souths, East and West")

    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('canceled', 'Canceled'),
        ('sold', 'Sold'),
    ], string='Estate Status', default='new')
    def action_lost_leads(self):
        pass