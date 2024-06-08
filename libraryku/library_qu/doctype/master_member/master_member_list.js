// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

// render
frappe.listview_settings['Master Member'] = {
	add_fields: ["name", "nama_member", "join_date", "member_type", "status_member"],
	get_indicator: function(doc) {
		if(doc.member_type === 'Bronze') {
			return [__("Bronze"), "darkgrey", "member_type,=,Bronze"];
		}else if (doc.member_type === 'Silver') {
			return [__("Silver"), "red", "member_type,=,Silver"];
		} else if (doc.member_type === 'Gold') {
			return [__("Gold"), "orange", "member_type,=,Gold"];
		}
	}
};
