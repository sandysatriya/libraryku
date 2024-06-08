# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "libraryku"
app_title = "Library Qu"
app_publisher = "MIS"
app_description = "Library Qu"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@mis.id"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/libraryku/css/libraryku.css"
# app_include_js = "/assets/libraryku/js/libraryku.js"

# include js, css files in header of web template
# web_include_css = "/assets/libraryku/css/libraryku.css"
# web_include_js = "/assets/libraryku/js/libraryku.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

doctype_js = {"Purchase Order" : "public/js/purchase_order.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "libraryku.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "libraryku.install.before_install"
# after_install = "libraryku.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "libraryku.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
    "Purchase Order" : {
        "validate": "libraryku.api.hello"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"libraryku.tasks.all"
# 	],
# 	"daily": [
# 		"libraryku.tasks.daily"
# 	],
# 	"hourly": [
# 		"libraryku.tasks.hourly"
# 	],
# 	"weekly": [
# 		"libraryku.tasks.weekly"
# 	]
# 	"monthly": [
# 		"libraryku.tasks.monthly"
# 	]
# }



# Testing
# -------

# before_tests = "libraryku.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "libraryku.event.get_events"
# }

fixtures = [
    {"doctype": "DocType", "filters": {"custom": 1}},
    "Custom Field",
    "Custom Script",
    "Property Setter",
    "Letter Head",
    {"doctype": "Print Format", "filters": {"standard": "No"}},
    {"doctype": "Report", "filters": {"standard": "No"}},
]