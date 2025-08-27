from django.urls import path, include
# استيراد العروض
from . import views

# مسارات التطبيق
urlpatterns = [
    path('', views.ProjectListView.as_view(), name='Project_list'),
    path('project/create/', views.ProjectCreateView.as_view(), name='Project_create'),
]