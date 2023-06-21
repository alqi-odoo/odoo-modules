from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re


class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registration_number"

    registration_number = fields.Char(
        string="Registration Number",
        required=True,
        default="MRN0000",
        copy=False,
    )
    vin = fields.Char(string="VIN", required=True)
    make = fields.Char(string="Make", compute="_compute_make")
    model = fields.Char(string="Model", compute="_compute_model")
    year = fields.Char(string="Year", compute="_compute_year")
    owner = fields.Many2one(
        comodel_name="res.partner",
        string="Owner",
        required=True,
        ondelete="cascade",
    )
    phone = fields.Char(related="owner.phone", string="Phone")
    email = fields.Char(related="owner.email", string="Email")
    picture = fields.Image(string="Picture")
    current_mileage = fields.Float(string="Current Mileage")
    license_plate = fields.Char(string="License Plate")
    certificate_title = fields.Image(string="Certificate of Title")
    registration_date = fields.Date(string="Registration Date")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("registration_number", "MRN0000") == "MRN0000":
                vals["registration_number"] = self.env["ir.sequence"].next_by_code(
                    "registration.number"
                )
        return super().create(vals_list)

    @api.constrains("vin")
    def _check_vin(self):
        for record in self:
            if not re.fullmatch("^[A-Z]{4}[0-9]{2}[A-Z0-9]{2}[0-9]{6}$", record.vin):
                raise ValidationError("VIN is invalid.")
            query = [("vin", "=", record.vin)]
            if self.env["motorcycle.registry"].search_count(query) > 1:
                raise ValidationError("VIN must be unique.")

    @api.constrains("license_plate")
    def _check_license_plate(self):
        for record in self:
            if record.license_plate and not re.fullmatch(
                "^[A-Z]{1,4}[0-9]{1,3}[A-Z]{0,2}$",
                record.license_plate,
            ):
                raise ValidationError("License plate is invalid.")

    @api.depends("vin")
    def _compute_make(self):
        for record in self:
            record.make = record.vin[:2]

    @api.depends("vin")
    def _compute_model(self):
        for record in self:
            record.model = record.vin[2:4]

    @api.depends("vin")
    def _compute_year(self):
        for record in self:
            record.year = record.vin[4:6]
