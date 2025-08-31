from django.urls import path, include
# استيراد العروض
from . import views

# مسارات التطبيق
urlpatterns = [
    path('', views.ProjectListView.as_view(), name='Project_list'),
    # اسم المسار Project_create
    path('project/create/', views.ProjectCreateView.as_view(), name='Project_create'),
    # آيد دي المشروع <int:pk>
    path('project/edit/<int:pk>', views.ProjectUpdateView.as_view(), name='Project_update'),
    path('project/delete/<int:pk>', views.ProjectDeleteView.as_view(), name='Project_delete'),
    path('task/create/', views.TaskCreateView.as_view(), name='Task_create'),
    path('task/edit/<int:pk>', views.TaskUpdateView.as_view(), name='Task_update'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name='Task_delete'),
]