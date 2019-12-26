from datetime import datetime, time

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError



class PurchaseReq(models.Model):
	_inherit='purchase.requisition'

	
	def _get_default_unit(self):

		user = self.env.user
		employee = self.env['hr.employee'].search([('user_id', '=' , user.id )])
		if not employee:
			raise UserError('No Employee linked to user %s!' % user.name)

		# if not employee.work_location:
		#     raise UserError('No Work Location for Employee %s!' % employee.name)
		# location = employee.work_location.code# analytic tag

		if not employee.department_id:
			raise UserError('No Department for Employee %s!' % employee.name )
		unit = employee.department_id.id #department
		return unit

	def _get_default_location(self):

		user = self.env.user
		employee = self.env['hr.employee'].search([('user_id', '=' , user.id )])
		if not employee:
			raise UserError('No Employee linked to user %s!' % user.name)

		if not employee.work_location:
		    raise UserError('No Work Location for Employee %s!' % employee.name)
		location = employee.work_location.id# analytic tag
		return location

		

	unit_id = fields.Many2one(readonly=True, comodel_name='hr.department', string='Unit',default=_get_default_unit)
	analytic_tag_ids = fields.Many2one(readonly=True ,comodel_name='account.analytic.tag', string='Location',default=_get_default_location)
