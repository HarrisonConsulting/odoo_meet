{
    "name": "Google Meet",
    "version": '17.0.0.0.1',
    "summary": "Integrates Google Meet Video Conferencing with Odoo Calendar Events",
    "description": """ 
        This module integrates Google Meet Video Conferencing with Odoo Calendar Events.
        It includes the necessary files and configurations to enable Google Meet for appointments when the location is left empty.
    """,
    "category": "Website",
    "author": "Harrison Consulting, LLC",
    "website": "https://www.harrison.consulting",
    'license': 'GPL-3',
    "depends": ["calendar", "google_calendar"],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
