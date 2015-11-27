#Odoo imports
from openerp import models, fields, api

class incomingorder(models.Model):
    _name = 'incomingorder.tracking'

    description = fields.Char('Item Description', required=True)
    grade = fields.Char('Grade', required=True)
    size = fields.Integer('Size', required=True)
    supplier = fields.Char('Supplier', required=True)
    stock = fields.Boolean('Stock')
    general = fields.Boolean('General')
    ponum = fields.Char('PO Number', required=True)
    podate = fields.Date('PO Date', required=True)
    porate = fields.Char('PO Rate/unit', required=True)
    invoicenum = fields.Char('Invoice Number', required=True)
    invoicedate = fields.Date('Invoice Date', required=True)
    invoicerate = fields.Char('Invoice Rate/unit', required=True)
    granno = fields.Char('GRAN No', required=True)
    inwardno = fields.Char('Inwardno', required=True)
    roomno = fields.Char('Room No', required=True)
    receiveddate = fields.Date('Received Date', required=True)
    vehicleno = fields.Char('Vehicle No', required=True)
    coilno = fields.Char('Coil No', required=True)

    state = fields.Selection([
            ('receipt', 'Goods Receipt'),
            ('counting', 'Goods Counting'),
            ('acceptance', 'Production Acceptance'),
            ('quality', 'Quality Check'),
            ('purchase', 'Purchase Register'),
            ('grn', 'GRN Prepared'),
            ],default='receipt')

    #This function is triggered when the user clicks on the button 'Set to receipt'
    @api.multi
    def receipt_progressbar(self):
      
	return {
		 'name': 'check order',
		 'type': 'ir.actions.act_window',
            'res_model': 'checkorder.tracking',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }

    #This function is triggered when the user clicks on the button 'Set to counting'
    @api.one
    def counting_progressbar(self):
	self.write({
	    'state': 'counting'
	})

    #This function is triggered when the user clicks on the button 'set to acceptance'
    @api.one
    def acceptance_progressbar(self):
	self.write({
	    'state': 'acceptance'
	})

    #This function is triggered when the user clicks on the button 'set to quality'
    @api.one
    def quality_progressbar(self):
	self.write({
	    'state': 'quality',
	})

    #This function is triggered when the user clicks on the button 'set to purchase'
    @api.one
    def purchase_progressbar(self):
	self.write({
	    'state': 'purchase',
	})


    #This function is triggered when the user clicks on the button 'set to grn'
    @api.one
    def grn_progressbar(self):
	self.write({
	    'state': 'grn',
	})



