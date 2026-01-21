# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Document Type Release - LATAM",
    "summary": "Enable/disable restricted LATAM document types and force their availability",
    "description": """
Document Type Release - LATAM Localization
==========================================

This module extends the Latin American localization to provide flexible management
of document types that may be restricted by default.

Key Features
------------
* **Activate/Deactivate Document Types**: Easily enable or disable document types
  that are restricted or inactive in the system.
* **Force Availability**: Override letter and AFIP responsibility restrictions
  to make specific document types always available.
* **Bulk Actions**: Perform mass activate, deactivate, or toggle operations
  on multiple document types at once.
* **Enhanced Views**: Complete view of all document types (active and inactive)
  with advanced filters and grouping options.
* **User Notifications**: Visual feedback confirmations for all actions performed.

Use Cases
---------
* Testing environments where you need access to all document types
* Special business scenarios requiring non-standard document availability
* Migration processes where document type flexibility is needed
* Administrative control over document type accessibility

This module is designed for Latin American localizations and requires
the l10n_latam_invoice_document module.
    """,
    "author": "Martin Zanello",
    "website": "https://github.com/zanello1234",
    "support": "zanello1234@github.com",
    "category": "Accounting/Localizations",
    "version": "18.0.1.1.0",
    "license": "LGPL-3",
    "price": 0.0,
    "currency": "EUR",
    "depends": [
        "base",
        "account",
        "l10n_latam_invoice_document",
    ],
    "data": [
        "views/l10n_latam_document_type_views.xml",
    ],
    "assets": {},
    "images": [
        "static/description/banner.png",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
