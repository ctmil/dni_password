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

class DniPasswordPartner(models.Model):
	_inherit = 'res.partner'

	def create_user(self):

		if not self.dni:
			raise ValidationError('Se requiere DNI para crear un usuario')
		if not self.email:
			raise ValidationError('Se requiere Email para crear un usuario')

		self.env['res.users'].create({
			'name': self.name,
			'login': self.email,
			'password': self.dni,
			'partner_id': self.id,
			'in_group_9': True
		})
