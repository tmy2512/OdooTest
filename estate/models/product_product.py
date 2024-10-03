# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re
from collections import defaultdict
from email.policy import default
from operator import itemgetter

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import float_compare, groupby
from odoo.tools.misc import unique


class ProductTemplate(models.Model):
    _inherit = "product.template"

    yeumy_khong = fields.Boolean(string='Co', default=True, )
