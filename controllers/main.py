from odoo import http
from odoo.http import request

class PurchaseOrderController(http.Controller):
    
    @http.route('/archive/', auth='public', type='json')
    def purchase_order_archive(self, **kw):
        failed_respone = {
            "result": {
            "archived_orders": False,
            "code": 404,
            "message": "Could not found"
            },
            # "jsonrpc": "2.0"
        }

        if kw['method'] != 'archive':
            return failed_respone

        try:
            request.env['purchase.order'].sudo().browse(kw['orders']).archive_purchase_order_list_view()
            return {
                    "result": {
                    "archived_orders": kw['orders'],
                    "code": 200,
                    "message": "Successful"
                },
                    # "jsonrpc": "2.0"
            }
        except:
            return failed_respone
                



