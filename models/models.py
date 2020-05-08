# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class DniPassword(models.Model):
	_inherit = 'res.users'

	def dni_password(self):
		if self.partner_id.dni:
			self.password = self.partner_id.dni
		else:
			raise ValidationError('Este usuario no tiene DNI cargado')
