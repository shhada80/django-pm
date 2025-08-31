from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# استيراد النماذج
from . import models
from . import forms


# Create your views here.
class ProjectListView(ListView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Project
    # القالب المرتبط مع هذه النافذة
    template_name = 'project/list.html'

# إنشاء المشروع
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

# تعديل المشروع
class ProjectUpdateView(UpdateView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Project
    # نحدد الاستمارة
    # نحدد النموذج المرتبط مع هذه النافذة
    form_class = forms.ProjectUpdateForm
    # القالب المرتبط مع هذه النافذة
    template_name = 'project/update.html'
    # رابط إعادة التوجيه، وهو الصفحة الرئيسية أو قائمة المشاريع
    # success_url = reverse_lazy('Project_list')

    # لإعادة التوجيه لصفحة المشروع ذاته
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.id])

# حذف المشروع
class ProjectDeleteView(DeleteView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Project
    # القالب المرتبط مع هذه النافذة
    template_name = 'project/delete.html'
    # رابط إعادة التوجيه، وهو الصفحة الرئيسية أو قائمة المشاريع
    success_url = reverse_lazy('Project_list')

# إنشاء مهمة
class TaskCreateView(CreateView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Task
    # الحقول المطلوبة عند إنشاء المهمة
    fields = ['project', 'description']
    # نريد post فقط، ولا نريد عرض صفحة إنشاء المهمة
    http_method_names = ['post']
   # لإعادة التوجيه لصفحة المشروع
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])

# تحديث مهمة
class TaskUpdateView(UpdateView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Task
    # الحقول المطلوبة عند إنشاء المهمة
    fields = ['is_completed']
    # نريد post فقط، ولا نريد عرض صفحة إنشاء المهمة
    http_method_names = ['post']
   # لإعادة التوجيه لصفحة المشروع
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])

# حذف مهمة
class TaskDeleteView(DeleteView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Task

   # لإعادة التوجيه لصفحة المشروع
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])