# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

"""
LATAM Document Type Extension for Document Type Release
========================================================

This module extends the l10n_latam.document.type model to add functionality
for forcing document availability and managing document type states through
user-friendly actions with visual notifications.
"""

from odoo import models, fields, api, _


class L10nLatamDocumentType(models.Model):
    """Extension of LATAM Document Type with force availability feature.
    
    This class adds a 'force_available' flag to document types, allowing
    administrators to make specific document types available regardless of
    the standard AFIP responsibility and letter restrictions.
    
    Additionally, it provides server actions for bulk management of document
    type states with user-friendly notification feedback.
    """
    
    _inherit = 'l10n_latam.document.type'

    force_available = fields.Boolean(
        string='Force Availability',
        default=False,
        help='If checked, this document type will be available in invoices '
             'regardless of AFIP letter or responsibility restrictions. '
             'Use with caution in production environments.'
    )

    def action_activate(self):
        """Activate the selected document types.
        
        Sets active=True for all selected records and displays a success
        notification to the user indicating how many documents were activated.
        
        Returns:
            dict: Action dictionary for displaying notification
        """
        self.write({'active': True})
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Documents Activated'),
                'message': _('%s document(s) have been activated.') % len(self),
                'type': 'success',
                'sticky': False,
            }
        }

    def action_deactivate(self):
        """Deactivate the selected document types.
        
        Sets active=False for all selected records and displays a warning
        notification to the user indicating how many documents were deactivated.
        
        Returns:
            dict: Action dictionary for displaying notification
        """
        self.write({'active': False})
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Documents Deactivated'),
                'message': _('%s document(s) have been deactivated.') % len(self),
                'type': 'warning',
                'sticky': False,
            }
        }

    def action_toggle_active(self):
        """Toggle the active state of selected document types.
        
        For each selected record, switches the active state from True to False
        or vice versa. Displays an info notification to the user.
        
        Returns:
            dict: Action dictionary for displaying notification
        """
        for record in self:
            record.active = not record.active
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Status Updated'),
                'message': _('The status of %s document(s) has been toggled.') % len(self),
                'type': 'info',
                'sticky': False,
            }
        }

    def action_force_available(self):
        """Force availability for the selected document types.
        
        Sets force_available=True for all selected records. Documents with
        forced availability will appear in invoice document type selection
        regardless of AFIP restrictions.
        
        Returns:
            dict: Action dictionary for displaying notification
        """
        self.write({'force_available': True})
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Availability Forced'),
                'message': _('%s document(s) will now be available without restrictions.') % len(self),
                'type': 'success',
                'sticky': False,
            }
        }

    def action_remove_force_available(self):
        """Remove forced availability from selected document types.
        
        Sets force_available=False for all selected records. Documents will
        return to normal restriction behavior based on AFIP responsibility
        and letter rules.
        
        Returns:
            dict: Action dictionary for displaying notification
        """
        self.write({'force_available': False})
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Normal Availability'),
                'message': _('%s document(s) will return to normal restrictions.') % len(self),
                'type': 'warning',
                'sticky': False,
            }
        }
