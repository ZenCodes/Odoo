from openerp import models, fields, api, tools


class Grnflow(models.Model):


    _inherit = "stock.move"

    _columns = {
        'partner_id': fields.related('partner_id','RTN',type="char",relation="res.partner",string="Supplier",store=True,readonly=True),
        'price_unit': fields.related('price_unit','RTN',type="char",relation="purchase.order",string="PO Rate",store=True,readonly=True),
        'product_qty': fields.related('price_qty','RTN',type="char",relation="purchase.order.line",string="Quantity",store=True,readonly=True),
	'date_order': fields.related('date_order','RTN',type="datetime",relation="purchase.order",string="PO Date",store=True,readonly=True),
        'date_invoice': fields.related('date_invoice','RTN',type="date",relation="account.invoice",string="Invoice Number",store=True,readonly=True)
	
 	
    }
    
    size = fields.Integer(string='Size')
    grade = fields.Char(string='Grade')
    stock = fields.Boolean('Stock')
    general = fields.Boolean('General')    
    ponum = fields.Char('PO Number')
    podate = fields.Date('PO Date')
    porate = fields.Char('PO Rate/unit')
    invoicenum = fields.Char('Invoice Number')
    invoicedate = fields.Date('Invoice Date')
    invoicerate = fields.Char('Invoice Rate/unit')

    state = fields.Selection([
('goods_receipt', "Goods Receipt"),
('goods_counting', "Goods Counting"),
('product_acceptance', "Product Acceptance"),
('quality_check', "Quality Check"),
('purchase_register', "Purchase Register"),
('grn_prepared', "GRN prepared")],default='goods_receipt')
    

    