# -*- coding: utf-8 -*-
{
    "name": "Product Catalog - Stock",
    "summary": "Add menu item linking to product catalog to inventory app.",
    "description": """
        Add menu item linking to product catalog to inventory app.
    """,
    "author": "Samuel Ochoa",
    "maintainer": "Samuel Ochoa",
    "website": "https://s8a.github.io",
    "category": "Technical",
    "version": "0.1",
    "application": False,
    "auto_install": True,
    "license": "LGPL-3",
    "depends": [
        "stock",
        "s8a_product_catalog",
    ],
    "data": [
        "views/product_views.xml",
    ],
}
