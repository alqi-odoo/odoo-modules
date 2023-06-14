from odoo import fields, models


class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"

    registry_number = fields.Char(string="Registry Number", required=True)
    vin = fields.Char(string="VIN", required=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    picture = fields.Image(string="Picture")
    current_mileage = fields.Float(string="Current Mileage")
    license_plate = fields.Char(string="License Plate")
    certificate_title = fields.Image(string="Certificate of Title")
    register_date = fields.Date(string="Register Date")
