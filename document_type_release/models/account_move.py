# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

"""
Account Move Extension for Document Type Release
=================================================

This module extends the account.move model to include document types
that have been marked with 'force_available' flag, making them accessible
regardless of standard LATAM letter/responsibility restrictions.
"""

from odoo import models, api


class AccountMove(models.Model):
    """Extension of Account Move to support forced document type availability.
    
    This class overrides the document type computation to include document types
    that have been explicitly marked as 'force_available', bypassing the standard
    AFIP responsibility and letter restrictions used in Latin American localizations.
    """
    
    _inherit = 'account.move'

    @api.depends('journal_id', 'partner_id', 'company_id', 'move_type', 'debit_origin_id')
    def _compute_l10n_latam_available_document_types(self):
        """Compute available document types including forced availability documents.
        
        This method extends the standard document type computation to include
        document types that have 'force_available' set to True. These documents
        will appear in the selection regardless of AFIP responsibility restrictions.
        
        The method:
        1. Calls the parent computation to get standard available documents
        2. Searches for documents with force_available=True for the company's country
        3. Filters by internal_type based on the move_type (invoice, credit_note, debit_note)
        4. Merges the forced documents with the standard available documents
        
        Returns:
            None: Updates l10n_latam_available_document_type_ids on each record
        """
        super()._compute_l10n_latam_available_document_types()
        
        # Add documents with force_available=True
        for rec in self.filtered(lambda x: x.journal_id and x.l10n_latam_use_documents):
            # Get forced documents for the company's fiscal country
            forced_docs = self.env['l10n_latam.document.type'].search([
                ('force_available', '=', True),
                ('active', '=', True),
                ('country_id', '=', rec.company_id.account_fiscal_country_id.id),
            ])
            
            # Filter by internal_type based on move_type
            if rec.move_type in ['out_refund', 'in_refund']:
                internal_types = ['credit_note', 'all']
            elif rec.move_type in ['out_invoice', 'in_invoice']:
                internal_types = ['invoice', 'debit_note', 'all']
            else:
                internal_types = ['all']
            
            # Override for debit origin
            if rec.debit_origin_id:
                internal_types = ['debit_note', 'all']
            
            forced_docs = forced_docs.filtered(
                lambda d: d.internal_type in internal_types
            )
            
            # Merge forced documents with available documents
            if forced_docs:
                rec.l10n_latam_available_document_type_ids = (
                    rec.l10n_latam_available_document_type_ids | forced_docs
                )
