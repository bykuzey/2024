from odoo import http


class ProductCatalogController(http.Controller):

    def _get_product_template_domain(self):
        return [("sale_ok", "=", True)]

    @http.route("/s8a/product_catalog", auth="public", website=True)
    def product_catalog(self, **kwargs):
        domain = self._get_product_template_domain()
        products = http.request.env["product.template"].sudo().search(domain)
        context = {
            "products": products,
        }
        return http.request.render("s8a_product_catalog.product_catalog", context)
