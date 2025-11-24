"""
URL configuration for projects_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# خاص بتعريب العبارات
from django.utils.translation import gettext as _

# تعديل عنوان لوحة التحكم من (إدارة جانغو) إلى (إدارة المشاريع)
admin.site.site_header = _('Projects Management')
# تعديل عنوان الصفحة الذي يظهر في شريط المتصفح (إدارة الموقع | إدارة موقع جانغو)
admin.site.site_title = _('Projects Management')

urlpatterns = [
    # إنشاء مسار جديد للتطبيق projects
    # تحديد مسار المشروع، ومسار المشروع الرئيسي يكفي أن نكتب /
    # ملف العناوين في التطبيق include("projects.urls"))
    path("", include("projects.urls")),
    path("accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
    # خاص بشرط التطوير
    # احذف أو عطّل debug_toolbar في الإنتاج
    # path('__debug__/', include(debug_toolbar.urls)),
]

# إضافة مسارات الملفات الثابتة
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)