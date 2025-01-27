{
    'name': 'QR Code Generator',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Generates a QR code from a given URL',
    'author': 'SIMI Technologies',
    'website': 'https://simitechnologies.co.ke',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/qr_code_views.xml',
    ],
    'installable': True,
    'application': True,
    'images': ['static/description/images/qr_code_genetator.png'],
    'license': 'LGPL-3',
}
