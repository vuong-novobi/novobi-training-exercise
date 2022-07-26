from odoo import api, models, fields, _
import datetime as dt
from odoo.exceptions import ValidationError, UserError

class PurchaseOrderEnhancement(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean(default=True)
    USPhoneNumber = fields.Char(string="Phone Number")
    lifespan = fields.Integer(string="Lifespan")

    @api.model
    def schelduled_archive(self):
        for record in self.search([('state','in',['done', 'cancel'])]):
            if dt.datetime.now() > record.write_date + dt.timedelta(days=record.lifespan):
                record.active = False

    def archive_purchase_order(self, api_call=False):
        if not self.env['res.users'].has_group('purchase.group_purchase_manager') and not api_call:
            raise UserError(_('You do not have permission to do this action!'))
        if self.filtered(lambda record: record.state not in ['cancel', 'done']):
            raise ValidationError(_('Archive is only used for Locked or Canceled order!'))
        self.write({'active': False})
    
    def unarchive_purchase_order(self):
        if not self.env['res.users'].has_group('purchase.group_purchase_manager'):
            raise UserError(_('You do not have permission to do this action!'))
        if self.filtered(lambda record: record.active == True):
            raise ValidationError(_('Unarchive is only used for archived order!'))
        self.write({'active': True})