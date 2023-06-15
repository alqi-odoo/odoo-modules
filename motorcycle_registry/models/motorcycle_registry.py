from odoo import fields, models


class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"

    registration_number = fields.Char(string="Registration Number", required=True)
    vin = fields.Char(string="VIN", required=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    picture = fields.Image(string="Picture")
    current_mileage = fields.Float(string="Current Mileage")
    license_plate = fields.Char(string="License Plate")
    certificate_title = fields.Image(string="Certificate of Title")
    registration_date = fields.Date(string="Registration Date")
