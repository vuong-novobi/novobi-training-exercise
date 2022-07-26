from odoo import models, fields, _
from odoo.exceptions import ValidationError

class ArchiveOldOrder(models.TransientModel):
    _name = "archive.old.order"
    _description = "Archive Old Order"

    purchase_order_list = fields.Many2many(comodel_name="purchase.order", domain=[('state','in',('done','cancel'))])
    #ids
    def action_archive_old_order(self):
        self.purchase_order_list.archive_purchase_order_form_view()
