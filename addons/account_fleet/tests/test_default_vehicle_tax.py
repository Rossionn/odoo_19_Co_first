# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import tagged

from odoo.addons.account.tests.common import AccountTestInvoicingCommon


@tagged('post_install', '-at_install')
class TestDefaultVehicleTax(AccountTestInvoicingCommon):

    def test_default_purchase_tax_loaded_from_vehicle(self):
        brand = self.env["fleet.vehicle.model.brand"].create({
            "name": "Audi",
        })
        model = self.env["fleet.vehicle.model"].create({
            "brand_id": brand.id,
            "name": "A3",
        })
        vehicle = self.env["fleet.vehicle"].create({
            "model_id": model.id,
            "plan_to_change_car": False,
            "default_purchase_tax_id": self.tax_purchase_a.id,
        })

        bill = self.init_invoice('in_invoice', products=self.product_a, post=False)
        line = bill.invoice_line_ids[0]
        line.vehicle_id = vehicle
        line._onchange_vehicle_id_set_default_purchase_tax()

        self.assertEqual(line.tax_ids, self.tax_purchase_a)
