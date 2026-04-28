from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    service_date_start = fields.Date(string='Date de début')
    service_date_end = fields.Date(string='Date de fin')
