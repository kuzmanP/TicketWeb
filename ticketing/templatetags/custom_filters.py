import base64
from io import BytesIO
from django import template
import qrcode

register = template.Library()

@register.filter
def get_qr_code_data(qr_code_value):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_code_value)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    image_stream = BytesIO()
    img.save(image_stream, format='PNG')
    image_stream.seek(0)

    image_data = base64.b64encode(image_stream.getvalue()).decode('utf-8')
    return image_data
