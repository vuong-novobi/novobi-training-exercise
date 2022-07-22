from odoo import api, models, fields, _
import datetime as dt
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    active = fields.Boolean(default=True)
    lifespan = fields.Integer(string='Lifespan')
    USPhoneNumber = fields.Char(string="Phone Number")

    def archive_purchase_order_form_view(self):
        for rec in self:
            rec.active = False

    def archive_purchase_order_list_view(self):
        for rec in self:
            if rec.state in ('cancel', 'done'):
                rec.active = False
            else:
                raise ValidationError(_('Archive is only used for Locked or Canceled order!'))

    @api.model
    def schelduled_archive(self):
        for record in self.search(['|',('state','=','cancel'), ('state','=','done')]):
            if dt.datetime.now() > record.write_date + dt.timedelta(days=record.lifespan):
                record.active = False