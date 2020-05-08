# -*- coding: utf-8 -*-
from odoo import http

# class DniPassword(http.Controller):
#     @http.route('/dni_password/dni_password/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dni_password/dni_password/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dni_password.listing', {
#             'root': '/dni_password/dni_password',
#             'objects': http.request.env['dni_password.dni_password'].search([]),
#         })

#     @http.route('/dni_password/dni_password/objects/<model("dni_password.dni_password"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dni_password.object', {
#             'object': obj
#         })