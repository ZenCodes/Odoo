#Odoo imports
from openerp import models, fields, api

class checkorder(models.Model):
    _name = 'checkorder.tracking'

    name = fields.Char('Product name', required=True)
    quantity = fields.Integer('Quantity', required=True)
    invoiceno = fields.Char('Invoice no', required=True)
    
    state = fields.Selection([
            ('counting', 'Goods Counting'),
            ('acceptance', 'Production Acceptance'),
            ('quality', 'Quality Check'),
            ('purchase', 'Purchase Register'),
            ('grn', 'GRN Prepared'),
            ],default='counting')


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



