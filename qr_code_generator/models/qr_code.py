import qrcode
from odoo import models, fields, api
from io import BytesIO
import base64
from odoo.exceptions import UserError


class QrCodeGenerator(models.Model):
    _name = 'qrcode.generator'
    _description = 'QR Code Generator'

    name = fields.Char('Name', required=True)
    url = fields.Char('URL', required=True)
    qr_code_image = fields.Image('QR Code Image', readonly=True)

    def generate_qr_code(self):
        for record in self:
            if not record.url:
                raise UserError("Please provide a valid URL for the QR code.")
            img = qrcode.make(record.url)
            img_byte_arr = BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            record.qr_code_image = base64.b64encode(img_byte_arr.read())

    def download_qr_code(self):
        for record in self:
            if record.qr_code_image:
                filename = f"{record.name}_qr_code.png"
                return {
                    'type': 'ir.actions.act_url',
                    'url': f'/web/content/{record._name}/{record.id}/qr_code_image?download=true&filename={filename}',
                    'target': 'self',
                }
            else:
                raise UserError("QR Code not generated yet. Please generate it first.")


