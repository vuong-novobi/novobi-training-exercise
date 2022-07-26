from odoo import models, fields

class PurchaseReport(models.Model):
    _inherit = "purchase.report"
    payment_term_id = fields.Many2one('account.payment.term', string='Payment Term', readonly=True)

    def _select(self):
        return super(PurchaseReport, self)._select() + ',po.payment_term_id as payment_term_id'

    def _group_by(self):
        return super(PurchaseReport, self)._group_by() + ', po.payment_term_id'