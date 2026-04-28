{
    'name': 'Account Mandatory Line Dates',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Accounting',
    'summary': 'Require start/end dates on invoice lines for selected accounts',
    'depends': ['account'],
    'data': [
        'views/account_account_views.xml',
        'views/account_move_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
}
