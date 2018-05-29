# -*- coding: utf-8 -*-
from openerp import SUPERUSER_ID

import openerp
from openerp import http
from openerp import fields, api, _
from openerp.http import request
from openerp.osv.orm import browse_record
from openerp.addons.website_sale.controllers.main import website_sale

class Webcomment(website_sale):

    @http.route(['/shop/confirm_order'], type='http', auth="public", website=True)
    def confirm_order(self, **post):
        cr, uid, context, registry = request.cr, request.uid, request.context, request.registry

        order = request.website.sale_get_order(context=context)
        if order:
            order.write({'comment': post.get('comment')})

        if not order:
            return request.redirect("/shop")

        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection

        values = self.checkout_values(post)

        values["error"], values["error_message"] = self.checkout_form_validate(values["checkout"])
        if values["error"]:
            return request.website.render("website_sale.checkout", values)

        self.checkout_form_save(values["checkout"])

        order.onchange_partner_shipping_id()
        order.order_line._compute_tax_id()

        request.session['sale_last_order_id'] = order.id
        request.session['comment'] = order.comment

        request.website.sale_get_order(update_pricelist=True, context=context)

        extra_step = registry['ir.model.data'].xmlid_to_object(cr, uid, 'website_sale.extra_info_option', raise_if_not_found=True)
        if extra_step.active:
            return request.redirect("/shop/extra_info")

        return request.redirect("/shop/payment")
