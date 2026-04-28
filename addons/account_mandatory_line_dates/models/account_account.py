from odoo import fields, models


class AccountAccount(models.Model):
    _inherit = 'account.account'

    require_invoice_line_date_range = fields.Boolean(
        string='Dates de début/fin obligatoires',
        help='Si activé, les lignes de facture utilisant ce compte doivent avoir une date de début et une date de fin.',
    )
