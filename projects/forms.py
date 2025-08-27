from django import forms
from . import models


class ProjectCreateForm(forms.ModelForm):
    # التصريح عن الصنف Meta
    class Meta:
        # النموذج المستهدف
        model = models.Project
        # تحديد الحقول المطلوبة في ههذ الاستمارة
        # لا نريد جميع الحقول لإدخالها، فحقل الحالة سيحدد تلقائياً عند إنشاء المشروع، وكذلك تاريخ الإنشاء والتحديث، والمستخدم صاحب المشروع
        fields = ['category', 'title', 'description']
        # تحديد الحقول
        widgets = {
            'category': forms.Select(),
            'title': forms.TextInput(),
            'description': forms.Textarea()
        }
