# استيراد بعض المكتبات الضرورية
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


attrs = {'class': 'form-control'}

# صياغة الاستمارة من خلال الأصناف
# الوراثة من صنف خاص يدعى AuthenticationForm حيث لدى جانغو تطبيق خاص بالمصادقة
class UserLoginForm(AuthenticationForm):

    # تحديد الدالة البانية وتمرير الاستمارة
    def __init__(self, *args, **kwargs):
        # استدعاء الدالة البانية للصنف الأب
        super(UserLoginForm, self).__init__(*args, **kwargs)

    # تعريف حقول الاستمارة
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs=attrs)
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs=attrs)
    )
    # بما أننا قمنا هنا بإعادة كتابة الاستمارة، فيجب علينا تعريف المسار لوجن ضمن urls.py وذلك لتحديد الاستمارة الجديدة


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label=_('First Name'),
        widget=forms.TextInput(attrs=attrs)
    )
    last_name = forms.CharField(
        label=_('Last Name'),
        widget=forms.TextInput(attrs=attrs)
    )
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs=attrs)
    )
    email = forms.EmailField(
        label=_('Email'),
        widget=forms.TextInput(attrs=attrs)
    )
    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )
    password2 = forms.CharField(
        label=_('Password Confirmation'),
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )

    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'username', 'email')


class ProfileForm(UserChangeForm):
    # إخفاء حقل كلمة السر
    password = None

    class Meta:
        # الموديل المطلوب
        model = User
        # الحقول المطلوبة
        fields = ['first_name', 'last_name', 'email']
        # إضافة كلاس بوستراب
        widgets = {
            'first_name': forms.TextInput(attrs=attrs),
            'last_name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs),
        }