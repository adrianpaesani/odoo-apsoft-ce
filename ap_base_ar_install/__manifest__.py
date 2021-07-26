##############################################################################
#
#    Copyright (C) 2021  AP Software
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Odoo Base Modules Install CE Argentinian Localization",
    "version": "13.0",
    "category": "Tools",
    "summary": "Install standard dependencies for Argentinian Localization (Adhoc) on Community Edition",
    "author": "Adrian Paesani",
    "website": "http://github.com/apaesani/ap_soft",
    "license": "AGPL-3",
    "depends": [
        # Instalamos la Localización Argentina y sus dependencias base
        # account_debit_note
        # l10n_ar
        # account_check
        # account_witholding
        # account_payment_group_document
        "l10n_ar_ux",
        # Instalamos las retenciones
        "l10n_ar_account_withholding",
        # Factura Electrónica Argentina 
        "l10n_ar_afipws_fe",
        # Instalamos el listado de bancos argentinos
        "l10n_ar_bank",
        # Tasa inversa para monedas
        "base_currency_inverse_rate",
        # Instalamos los reportes de IVA Compras/Ventas
        "l10n_ar_reports",
        # "l10n_ar_stock",  # Remito electrónico Argentino tiene una rara
        # dependencia con l10n_ar_account
        # "l10n_ar_report_stock", # OJO esto instala Stock
        # Para mejorar la usabilidad
        "base_ux",  # mejoras de base
        "product_ux",  # mejoras en productos
        "sale_ux",  # mejoras en ventas
        # "auto_backup",  # poner el backup en: /var/odoo/backups/
        # "mail_activity_board_ux",  # quitar actividades del chatter
        #"partner_ref_unique",  # evita duplicados en referencia
        #"partner_vat_unique",  # evita duplicados numeros de referencia
        #"product_unique",  # no se pueden duplicar codigos de producto
        "web_responsive",
    ],
    "data": [],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": False,
}