from django import forms
from . import models
# خاص بتعريب العبارات
from django.utils.translation import gettext as _

# نعرف attribute
attrs = {'class': 'form-control'}
# ثم نسندها (attrs=attrs) إلى كل حقل من الحقول التي لدينا في الأصناف التالية

# إنشاء المشروع
class ProjectCreateForm(forms.ModelForm):
    # التصريح عن الصنف Meta
    class Meta:
        # النموذج المستهدف
        model = models.Project
        # تحديد الحقول المطلوبة في هذه الاستمارة
        # لا نريد جميع الحقول لإدخالها، فحقل الحالة سيحدد تلقائياً عند إنشاء المشروع، وكذلك تاريخ الإنشاء والتحديث، والمستخدم صاحب المشروع
        fields = ['category', 'title', 'description']
        # تحديد العناوين
        labels = {
            'category': _('Category'),
            'title': _('Title'),
            'description': _('Description'),
        }

        # تحديد الحقول
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs=attrs)
        }

# تعديل المشروع
class ProjectUpdateForm(forms.ModelForm):
    # التصريح عن الصنف Meta
    class Meta:
        # النموذج المستهدف
        model = models.Project
        # تحديد الحقول المطلوبة في هذه الاستمارة
        fields = ['category', 'title', 'status']
        # تحديد الحقول
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'status': forms.Select(attrs=attrs)
        }