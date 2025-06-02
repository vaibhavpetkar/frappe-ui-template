import frappe
from frappe import _

def get_sidebar_items():
    """
    Get sidebar navigation items based on user permissions
    Returns modules and favorites for the sidebar
    """
    modules = []
    favorites = []
    
    # Get modules based on user permissions
    user_modules = frappe.get_list("Module Def", 
                                  fields=["name", "app_name", "icon"],
                                  filters={"restrict_to_domain": ["in", frappe.get_active_domains()]},
                                  order_by="name")
    
    for module in user_modules:
        modules.append({
            "name": module.name,
            "icon": module.icon or "octicon octicon-file-directory",
            "link": f"/app/{frappe.scrub(module.name)}"
        })
    
    # Get user favorites
    user_favorites = frappe.get_list("Desktop Icon",
                                    fields=["label", "link", "type", "icon", "module_name", "color"],
                                    filters={"standard": 0, "owner": frappe.session.user},
                                    order_by="idx")
    
    for favorite in user_favorites:
        favorites.append({
            "name": favorite.label,
            "icon": favorite.icon or "octicon octicon-file",
            "link": favorite.link,
            "color": favorite.color
        })
    
    return {"modules": modules, "favorites": favorites}

def get_navbar_items():
    """
    Get top navbar navigation items
    """
    navbar_items = [
        {"name": "Dashboard", "link": "/app/dashboard", "active": True},
        {"name": "Workspace", "link": "/app/workspace"},
        {"name": "Reports", "link": "/app/reports"},
        {"name": "Settings", "link": "/app/settings"}
    ]
    
    return navbar_items

def get_dashboard_data():
    """
    Get dashboard statistics and recent activities
    """
    stats = []
    activities = []
    
    # Get quick stats
    stats.append({
        "title": "Sales Orders",
        "value": frappe.db.count("Sales Order", {"docstatus": 1}),
        "link": "/app/sales-order"
    })
    
    stats.append({
        "title": "Customers",
        "value": frappe.db.count("Customer"),
        "link": "/app/customer"
    })
    
    stats.append({
        "title": "Open Tasks",
        "value": frappe.db.count("Task", {"status": "Open"}),
        "link": "/app/task"
    })
    
    # Get recent activities
    recent_docs = frappe.get_all("Activity Log", 
                               fields=["reference_doctype", "reference_name", "subject", "creation"],
                               filters={"operation": ["in", ["create", "submit", "update"]]},
                               order_by="creation desc",
                               limit=10)
    
    for doc in recent_docs:
        activities.append({
            "doctype": doc.reference_doctype,
            "name": doc.reference_name,
            "subject": doc.subject,
            "time": doc.creation,
            "link": f"/app/{frappe.scrub(doc.reference_doctype)}/{doc.reference_name}"
        })
    
    return {"stats": stats, "activities": activities}

def after_insert(doc, method=None):
    """
    Hook that runs after a document is inserted
    """
    # Add custom logic here if needed
    pass

def on_update(doc, method=None):
    """
    Hook that runs when a document is updated
    """
    # Add custom logic here if needed
    pass

def on_submit(doc, method=None):
    """
    Hook that runs when a document is submitted
    """
    # Add custom logic here if needed
    pass
