from odoo import http
from odoo.addons.s8a_product_catalog.controllers import product_catalog  # type: ignore


class ProductCatalogControllerNoPoS(product_catalog.ProductCatalogController):

    def _get_product_template_domain(self):
        domain = super()._get_product_template_domain()
        pos_category = http.request.env.ref("point_of_sale.product_category_pos")
        domain += [("categ_id", "!=", pos_category.id)]
        return domain
