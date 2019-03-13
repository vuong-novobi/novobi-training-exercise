Purchase Order Archive
================================================

Business Concepts
-----------------
On a Odoo system with a high volume of purchases, the number of purchase orders displayed in the list view can become huge.
We don't want to see canceled or locked purchase orders. If a purchase order is archived, it will be hidden from the purchase orders list view.

Also, the system should automatic archive the old canceled/locked purchase orders.

In the other hand, we're using ABC system, so we also want to archive canceled or locked orders by using HTTP request.

Technical Requirements
----------------------
#### Initial
- New module: **purchase_order_archive**
- Odoo V12
- Follow [Odoo Guidelines](https://www.odoo.com/documentation/12.0/reference/guidelines.html)
#### Model
- Add new field: **active (boolean, default=True)**
- Only allow archive the purchase orders with current status is **locked** or **canceled**
#### View
- Form:
    + Add smart button allows archive PO. See example: [res.partner](https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/views/res_partner_views.xml#L202)
- Tree:
    + Add field **active (invisible=True)**
    + Add smart button allows archive PO.
    + Add decoration **_muted_** for archived orders.
- Search:
    + Add filter for field **active**. See example: [res.partner](https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/views/res_partner_views.xml#L461)
#### Cron Job
- Define **lifespan** in config parameter.
- Add cron job for daily checking old purchase order with **lifespan** and archive those orders if the **_current date > write_date + lifespan_**
    
    
#### Controller
- Add route allows archive multiple purchase orders: `type='json', auth='public', csrf=False`

#### Widget (TBD)
- TBD


How to submit your works?
-------------------------
Create your own repository privately and add [haidinh-novobi](https://github.com/haidinh-novobi) as a contributor.