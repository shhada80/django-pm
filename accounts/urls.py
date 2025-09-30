# تهيئة ملف الروابط
from django.contrib.auth.views import LoginView
from django.urls import path, include
from accounts.forms import UserLoginForm
from accounts.views import RegisterView, edit_profile
from django.contrib.auth.views import LogoutView

# التصريح عن المصفوفة urlpatterns
# وضمنها نضمن مجموعة من الروابط والعناوين المقدمة من جانغو، وهي خاصة بعملية المصادقة
urlpatterns = [
    # بما أننا قمنا في forms.py بإعادة كتابة الاستمارة، فيجب علينا تعريف المسار لوجن ضمن urls.py وذلك لتحديد الاستمارة الجديدة
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', edit_profile, name='profile'),
    path('', include('django.contrib.auth.urls'))
]