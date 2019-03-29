Purchase Order Enhancement
================================================

Business Concepts
-----------------
On a Odoo system with a high volume of purchases, the number of purchase orders displayed in the list view can become huge.
We don't want to see canceled or locked purchase orders. If a purchase order is archived, it will be hidden from the purchase orders list view. The person who has manager profile can archive old orders.
The system should automatic archive the old canceled/locked purchase orders. In the other hand, we're using ABC system, so we also want to archive canceled or locked orders by using HTTP request.

Another improvements, we want to have the phone number in the US domestic format at the contact information and want to know what payment terms apply for these purchase orders at the reports.


Technical Requirements
----------------------
#### Initial
- New module: **purchase_order_enhancement**.
- Odoo V12.
- Follow [Odoo Guidelines](https://www.odoo.com/documentation/12.0/reference/guidelines.html).

#### Model
- Add new field: **active (checkbox, default=True)**.
- Only allow archive the purchase orders with current status is **locked** or **canceled**.

#### Security
- Only Purchase Manger can archive Purchase Order(s)

#### View
- Form:
    + Adding smart button allows archive Purchase Orders.
- Tree:
    + Adding smart button allows archive Purchase Orders.
    + Archived orders must be showed in the gray color.
- Search:
    + Add filter for field **active**.

#### Wizard
- Adding the wizard (under Purchase > Configuration) allows archive multiple Purchase Orders.

#### Cron Job
- Define **lifespan** and allows user can modify it.
- Add cron job for daily checking old purchase order with **lifespan** and archive those orders if **_current date > write date + lifespan_**

#### Controller
- Adding route allows archive multiple purchase orders

```
# INPUT:
{
    "params":{
        "method": "archive",
        "orders": [1, 8]
    }

}
# ====================================
# OUTPUT

# Success:
{
    "id": null,
    "result": {
        "archived_orders": [1, 8],
        "code": 200,
        "message": "Successful"
    },
    "jsonrpc": "2.0"
}

# Not found:
{
    "id": null,
    "result": {
        "archived_orders": false,
        "code": 404,
        "message": "Could not found"
    },
    "jsonrpc": "2.0"
}
```

Hint: Using Postman for testing.

#### Widget
- Define new widget `us_phone` for showing phone number as US domestic format.

#### Report
- PDF: Add `Payment Term` right next to `Order Date`.
- Purchase Analysis: Add `Payment Term` for pivot view.


How to submit your exercise?
---------------------------
Create your own repository privately, then add your mentor as a contributor.
