from openerp import models, fields ,api ,tools


class Grnflow(models.Model):

    _name = "stock.move"
    _inherit = "stock.move"

    _columns = {
        'partner_id': fields.related('partner_id','RTN',type="char",relation="res.partner",string="Supplier",store=True,readonly=True),
        'price_unit': fields.related('price_unit','RTN',type="char",relation="purchase.order",string="PO Rate",store=True,readonly=True),
        'product_qty': fields.related('price_qty','RTN',type="char",relation="purchase.order.line",string="Quantity",store=True,readonly=True),
	'date_planned': fields.related('date_planned','RTN',type="date",relation="purchase.order.line",string="PO Date",store=True,readonly=True),
        'date_invoice': fields.related('date_invoice','RTN',type="date",relation="account.invoice",string="Invoice Number",store=True,readonly=True)
	
 	
    }
      

    my_field = fields.Char(string='My Field')
    size = fields.Integer(string='Size')
    grade = fields.Char(string='Grade')

    
    state = fields.Selection([('draft', 'New'),
				  ('goods_receipt', "Goods Receipt"),
				  ('goods_counting', "Goods Counting"),
				  ('product_acceptance', "Product Acceptance"),
				  ('quality_check', "Quality Check"),
				  ('purchase_register', "Purchase Register"),
				  ('grn_prepared', "GRN prepared"),
                                   ('cancel', 'Cancelled'),
                                   ('waiting', 'Waiting Another Move'),
                                   ('confirmed', 'Waiting Availability'),
                                   ('assigned', 'Available'),
                                   ('done', 'Done')
                                   ]) 

    @api.one
    def goods_counting(self):
	self.write({
	    'state': 'goods_counting'
	})

    
    