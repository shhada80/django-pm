from django import forms
from . import models

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