from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Master"),
			"items": [
				{
					"type": "doctype",
					"name": "Master Buku",
					"label": _("Master Buku 1"),
				},
				{
					"type": "doctype",
					"name": "Master Member"
				},
                {
					"type": "doctype",
					"name": "Master Tipe Buku"
				},
				{
					"type": "doctype",
					"name": "Sales Order",
					"label": _("Sales Confirmation"),
				},
			]
		},
        {
			"label": _("Transaction"),
			"items": [
				{
					"type": "doctype",
					"name": "Request Pinjaman"
				},
				{
					"type": "doctype",
					"name": "Pinjaman"
				},
				{
					"type": "doctype",
					"name": "Pengembalian"
				}
			]
		}
    ]