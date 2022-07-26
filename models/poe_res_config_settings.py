from odoo import models, fields

class ResConfigSettingsEnhancement(models.TransientModel):
    _inherit = 'res.config.settings'
    
    default_lifespan = fields.Integer(string="Lifespan", default_model='purchase.order')