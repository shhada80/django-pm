from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
# استيراد النماذج
from . import models
from . import forms


# Create your views here.
class ProjectListView(ListView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Project
    # القالب المرتبط مع هذه النافذة
    template_name = 'project/list.html'

class ProjectCreateView(CreateView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Project
    # نحدد الاستمارة
    # نحدد النموذج المرتبط مع هذه النافذة
    form_class = forms.ProjectCreateForm
    # القالب المرتبط مع هذه النافذة
    template_name = 'project/create.html'
    # رابط إعادة التوجيه، وهو الصفحة الرئيسية أو قائمة المشاريع
    success_url = reverse_lazy('Project_list')
