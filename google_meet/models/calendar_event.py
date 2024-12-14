from odoo import models, api

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    @api.model_create_multi
    def create(self, vals_list):
        enable_google_meet_global = self.env['ir.config_parameter'].sudo().get_param('appointment.enable_google_meet', default=False)
        enable_google_meet_global = bool(enable_google_meet_global)
        
        for vals in vals_list:
            # Check if Google Meet is enabled and location_id is empty
            if enable_google_meet_global and not vals.get('location'):
                vals['videocall_location'] = False
        
        return super().create(vals_list)