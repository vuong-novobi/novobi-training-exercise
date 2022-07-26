from odoo import http
from odoo.http import request
class PurchaseOrderController(http.Controller):
    
    @http.route('/archive/', auth='public', type='json')
    def purchase_order_archive(self, **kw):
        if kw.get('method') != 'archive':
            return {
                    "archived_orders": False,
                    "code": 400,
                    "message": f"Method is not supported: '{kw.get('method')}'"}

        po_obj = request.env['purchase.order']
        po_ids = kw.get('orders')

        if po_ids:
            check = list(set(po_ids)-set(po_obj.sudo().search([]).ids))
            if check:
                return {
                    "archived_orders": False,
                    "code": 401,
                    "message": f"Could not found purchase order id {check}!"}
            
            try:
                po_obj.sudo().browse(po_ids).archive_purchase_order(api_call=True)
                return {
                        "archived_orders": po_ids,
                        "code": 200,
                        "message": "Successful"}
            except:
                failed_ids = po_obj.sudo().browse(po_ids).filtered(lambda record: record.state not in ['cancel', 'done']).ids
                return {
                        "archived_orders": False,
                        "code": 402,
                        "message": f"Could not archive! Given purchase order id {failed_ids} not in 'Locked' or 'Canceled' status!"}

        return {
                "archived_orders": False,
                "code": 403,
                "message": "No purchase orders to archive!"}