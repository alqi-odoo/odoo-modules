{
    "name": "Motorcycle Registry",
    "summary": "Manage registration of motorcycles",
    "description": """Motorcycle Registry
====================
This module is used to keep track of the motorcycle registration and ownership of each motorcycle of the brand.""",
    "license": "LGPL-3",
    "author": "alqi-odoo",
    "website": "https://github.com/alqi-odoo/odoo-modules",
    "category": "Kawiil",
    "depends": ["base"],
    "data": [
        "security/motorcycle_registry_groups.xml",
        "security/ir.model.access.csv",
        "views/motorcycle_registry_menuitems.xml",
    ],
    "demo": [
        "demo/motorcycle_registry_demo.xml",
    ],
    "application": True,
}
