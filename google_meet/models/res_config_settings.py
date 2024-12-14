# File: models/appointment_type.py

from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    enable_google_meet = fields.Boolean(
        string="Enable Google Meet",
        help="Check this box to enable Google Meet Video Conferencing for all appointments when location is left empty",
        config_parameter="appointment.enable_google_meet",
    )