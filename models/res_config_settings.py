# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    crm_use_lead = fields.Boolean(
        string="Use Leads",
        config_parameter='crm.use_lead'
    )
