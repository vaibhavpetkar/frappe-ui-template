/**
 * Frappe ERPNext Integration Hooks
 * This file contains hooks to integrate the custom UI with ERPNext backend
 */

app_name = "frappe_ui_template"
app_title = "Frappe UI Template"
app_publisher = "Custom UI"
app_description = "Custom UI Template for Frappe ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@example.com"
app_license = "MIT"

# Include custom CSS and JS in every page
app_include_css = [
    "/assets/frappe_ui_template/css/custom_theme.css"
]
app_include_js = [
    "/assets/frappe_ui_template/js/custom_theme.js"
]

# Override standard templates
override_doctype_class = {
    # "DocType": "path.to.extended.class"
}

# Override standard templates
override_whitelisted_methods = {
    # "frappe.desk.doctype.event.event.get_events": "frappe_ui_template.event.get_events"
}

# Template overrides
jenv = {
    "methods": [
        "get_sidebar_items:frappe_ui_template.utils.get_sidebar_items",
        "get_navbar_items:frappe_ui_template.utils.get_navbar_items",
        "get_dashboard_data:frappe_ui_template.utils.get_dashboard_data"
    ]
}

# Fixtures to include in the app
fixtures = [
    {
        "dt": "Custom Field",
        "filters": [["module", "=", "Frappe UI Template"]]
    },
    {
        "dt": "Custom Script",
        "filters": [["module", "=", "Frappe UI Template"]]
    },
    {
        "dt": "Client Script",
        "filters": [["module", "=", "Frappe UI Template"]]
    }
]

# Document Events
doc_events = {
    "*": {
        "after_insert": "frappe_ui_template.utils.after_insert",
        "on_update": "frappe_ui_template.utils.on_update",
        "on_submit": "frappe_ui_template.utils.on_submit",
    }
}

# Website Settings
website_context = {
    "favicon": "/assets/frappe_ui_template/img/favicon.ico",
    "splash_image": "/assets/frappe_ui_template/img/splash.png"
}
