import frappe

@frappe.whitelist()
def get_buku(id_buku):
    get_buku = frappe.get_doc("Master Buku", id_buku)
    frappe.response['code'] = 200
    frappe.response['data'] = get_buku



@frappe.whitelist()
def insert_buku(nama_buku,tipe_buku, tahun_cetak):
    new_buku = frappe.new_doc("Master Buku")
    new_buku.nama_buku = nama_buku
    new_buku.tipe_buku = tipe_buku
    new_buku.tahun_cetak_buku = tahun_cetak
    new_buku.save()
    frappe.response['code'] = 200
    frappe.response['data'] = new_buku


@frappe.whitelist()
def delete_buku(id_buku):
    buku = frappe.get_doc("Master Buku", id_buku)
    buku.delete()
    frappe.response['code'] = 200
    frappe.response['data'] = "Sukses"


# @frappe.whitelist()
def hello(doc, event):
    new_emp = frappe.new_doc("Employee")
    new_emp.first_name = "Sandy"
    new_emp.gender = "Laki2"
    new_emp.date_of_birth = "2019-04-15"
    new_emp.date_of_joining = "2020-04-25"
    new_emp.save()