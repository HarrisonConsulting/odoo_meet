# Odoo Google Meet Integration

This module integrates Google Meet Video Conferencing with Odoo Calendar Events, automatically creating Google Meet links for calendar appointments when no location is specified.

## Features

- Seamless integration between Odoo Calendar Events and Google Meet
- Global configuration option to enable/disable Google Meet integration
- Automatic creation of video conference links when location is empty
- Works in conjunction with Google Calendar synchronization

## Requirements

- Odoo 17.0
- Google Calendar module (`google_calendar`) installed and configured
- Valid Google Workspace account with Meet access

## Installation

1. Clone this repository into your Odoo addons directory:
```bash
git clone https://github.com/HarrisonConsulting/odoo_meet.git
```

2. Update your Odoo addons list in Apps menu
3. Find and install "Google Meet" module

## Configuration

1. Go to Settings → General Settings
2. Locate the "Google Calendar" section
3. Enable "Google Meet Appointments" checkbox
4. Save settings

## Usage

Once enabled, the module will automatically:
- Create Google Meet links for new calendar events when no location is specified
- Display the video conferencing links in calendar event details
- Include Meet links in calendar invitations

## Technical Details

The module extends the following Odoo models:
- `calendar.event`: Adds Google Meet integration logic
- `res.config.settings`: Adds global configuration options

## License

This module is licensed under the [AGPL-3.0 License](https://www.gnu.org/licenses/agpl-3.0.html).

## Support

For support, please contact:
- Website: https://www.harrison.consulting
- Email: [info@harrison.consulting](mailto:info@harrison.consulting)

## Author

Harrison Consulting, LLC

---

Feel free to contribute to this project by submitting issues or pull requests.