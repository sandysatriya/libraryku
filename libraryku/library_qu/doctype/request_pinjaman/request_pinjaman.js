// Copyright (c) 2019, MIS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Request Pinjaman', {
	refresh: function (frm) {
		frm.add_custom_button(__('Button'), function () {
			frappe.msgprint('Hei')
		}, __("Make"));
		frm.add_custom_button(__('Button1'), function () {
			frappe.msgprint('Hei')
		}, __("Make"));
	},
	tanggal_pinjam: function (frm) {
		if (frm.doc.tanggal_pinjam < get_today()) {
			frm.set_value('tanggal_pinjam', '');
			frm.set_value('estimasi_tanggal_kembali', '');
			frappe.throw(__('Tidak Bisa Memilih Tanggal Terdahulu'));
		}
		frappe.call({
			method: "frappe.client.get",
			args: {
				doctype: "Master Member",
				name: frm.doc.id_member
			},
			callback: function (r) {
				if (r.message.member_type == 'Bronze') {
					frm.set_value('estimasi_tanggal_kembali', frappe.datetime.add_days(frm.doc.tanggal_pinjam, 3));
				} else if (r.message.member_type == 'Silver') {
					frm.set_value('estimasi_tanggal_kembali', frappe.datetime.add_days(frm.doc.tanggal_pinjam, 5));
				} else {
					frm.set_value('estimasi_tanggal_kembali', frappe.datetime.add_days(frm.doc.tanggal_pinjam, 7));
				}
			}
		});
	}
});


cur_frm.set_query('code_buku', 'request_line', function (doc, cdt, cdn) {
	var d = locals[cdt][cdn];
	return {
		filters: [
			['Master Buku', 'status', '=', 'Available']
		]
	}
});