from odoo import _, models
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        self._check_required_line_date_ranges()
        return super().action_post()

    def _check_required_line_date_ranges(self):
        for move in self.filtered(lambda m: m.is_invoice(include_receipts=True)):
            invalid_lines = move.invoice_line_ids.filtered(
                lambda line: (
                    line.display_type == 'product'
                    and line.account_id.require_invoice_line_date_range
                    and (not line.service_date_start or not line.service_date_end)
                )
            )
            if invalid_lines:
                account_codes = ', '.join(invalid_lines.mapped('account_id.code'))
                raise ValidationError(_(
                    "Vous ne pouvez pas valider cette facture. "
                    "Veuillez renseigner une date de début et une date de fin "
                    "sur les lignes utilisant les comptes: %(account_codes)s."
                ) % {
                    'account_codes': account_codes,
                })
