from odoo import models, fields


class JobSeeker(models.Model):
    _name = 'irada.job.seeker'
    _description = 'باحث عن عمل'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='الاسم الكامل', required=True, tracking=True)
    phone = fields.Char(string='رقم الجوال', tracking=True)
    email = fields.Char(string='البريد الإلكتروني')

    disability_type = fields.Selection([
        ('physical', 'إعاقة حركية'),
        ('visual', 'إعاقة بصرية'),
        ('hearing', 'إعاقة سمعية'),
        ('cognitive', 'إعاقة ذهنية/تعليمية'),
        ('other', 'أخرى'),
    ], string='نوع الإعاقة', tracking=True)

    skills = fields.Text(string='المهارات والخبرات')

    state = fields.Selection([
        ('available', 'متاح'),
        ('in_process', 'قيد التقديم'),
        ('hired', 'تم التوظيف'),
    ], string='الحالة', default='available', tracking=True)