{

    'name': 'إرادة - منصة توظيف',
    'version': '1.0',
    'summary': 'منصة توظيف عن بعد تمكّن أصحاب الهمم من الوصول لفرص عمل مناسبة',
    'category': 'Human Resources',
    'author': 'Elbashir',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/job_seeker_views.xml',
    ],
    'assets': {
    'web.assets_backend': [
        'irada_jobs/static/src/scss/irada_theme.scss',
        'irada_jobs/static/src/js/font_loader.js',
    ],},
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

