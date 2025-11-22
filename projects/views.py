from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# استيراد النماذج
from . import models
from . import forms

# الصنف LoginRequiredMixin مهم حتى لا نسمح بإضافة مشروع إلا للمسجلين
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Project
    # القالب المرتبط مع هذه النافذة
    template_name = 'project/list.html'
    # عرض 6 مشاريع فقط ضمن الصحفة الواحدة
    paginate_by = 6


    # خاص بفورم البحث
    # تخصيص الاستعلام
    def get_queryset(self):
        # نحصل على قائمة المشاريع
        query_set = super().get_queryset()
        # تعريف قائمة لاحتواء الشروط المطلوبة
        # يظهر لكل مستخدم مشاريعه فقط
        where = {'user_id': self.request.user}
        # يظهر لكل مستخدم مشاريعه ومشاريع غيره
        # where = {}

        # هل كلمة البحث ضمن الطلب
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        # إنشاء الاستعلام وتمرير الشروط
        return query_set.filter(**where)



# إنشاء المشروع
class ProjectCreateView(LoginRequiredMixin, CreateView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Project
    # نحدد الاستمارة
    # نحدد النموذج المرتبط مع هذه النافذة
    form_class = forms.ProjectCreateForm
    # القالب المرتبط مع هذه النافذة
    template_name = 'project/create.html'
    # رابط إعادة التوجيه، وهو الصفحة الرئيسية أو قائمة المشاريع
    success_url = reverse_lazy('Project_list')

    # التحقق من بيانات الاستمارة
    def form_valid(self, form):
        # المستخدم صاحب المشروع أو صاحب الطلب
        # عند حفظ المشروع سنحفظ آي دي المستخدم
        form.instance.user = self.request.user # آي دي المستخدم
        # استدعاء الدالة الأصلية
        return super().form_valid(form)

# تعديل المشروع
class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    # التحقق من المستخدم قبل عرض الصفحة
    # لا يجوز تعديل مشروع ليس من مشاريع المستخدم الحالي
    def test_func(self):
        # مقارنة آي دي المستخدم صاحب المشروع مع آي دي المستخدم الحالي صاحب الطلب
        # افتح الصفحة إذا كانت القيمة هي True
        # وإلا فلا تفتحها؛ لأن هذا يعني المشروع ليس للمستخدم الحالي
        return self.get_object().user_id == self.request.user.id

# حذف المشروع
class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Project
    # القالب المرتبط مع هذه النافذة
    template_name = 'project/delete.html'
    # رابط إعادة التوجيه، وهو الصفحة الرئيسية أو قائمة المشاريع
    success_url = reverse_lazy('Project_list')

    # لا يجوز تعديل مشروع ليس من مشاريع المستخدم الحالي
    def test_func(self):
        # مقارنة آي دي المستخدم صاحب المشروع مع آي دي المستخدم الحالي صاحب الطلب
        # افتح الصفحة إذا كانت القيمة هي True
        # وإلا فلا تفتحها؛ لأن هذا يعني المشروع ليس للمستخدم الحالي
        return self.get_object().user_id == self.request.user.id

# إنشاء مهمة
class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Task
    # الحقول المطلوبة عند إنشاء المهمة
    fields = ['project', 'description']
    # نريد post فقط، ولا نريد عرض صفحة إنشاء المهمة
    http_method_names = ['post']
   # لإعادة التوجيه لصفحة المشروع
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])

    # لا يجوز تعديل مشروع ليس من مشاريع المستخدم الحالي
    def test_func(self):
        # مقارنة آي دي المستخدم صاحب المشروع مع آي دي المستخدم الحالي صاحب الطلب
        # افتح الصفحة إذا كانت القيمة هي True
        # وإلا فلا تفتحها؛ لأن هذا يعني المشروع ليس للمستخدم الحالي
        # تحديد آي دي المشروع، ونحصل عليه من كائن الطلب
        project_id = self.request.POST.get('project', '')
        return models.Project.objects.get(pk=project_id).user_id == self.request.user.id

# تحديث مهمة
class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Task
    # الحقول المطلوبة عند إنشاء المهمة
    fields = ['is_completed']
    # نريد post فقط، ولا نريد عرض صفحة إنشاء المهمة
    http_method_names = ['post']
   # لإعادة التوجيه لصفحة المشروع
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])

    # لا يجوز تعديل مشروع ليس من مشاريع المستخدم الحالي
    def test_func(self):
        # مقارنة آي دي المستخدم صاحب المشروع مع آي دي المستخدم الحالي صاحب الطلب
        # افتح الصفحة إذا كانت القيمة هي True
        # وإلا فلا تفتحها؛ لأن هذا يعني المشروع ليس للمستخدم الحالي
        return self.get_object().project.user_id == self.request.user.id

# حذف مهمة
class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # نحدد النموذج المرتبط مع هذه النافذة
    model = models.Task

   # لإعادة التوجيه لصفحة المشروع
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])

    # لا يجوز تعديل مشروع ليس من مشاريع المستخدم الحالي
    def test_func(self):
        # مقارنة آي دي المستخدم صاحب المشروع مع آي دي المستخدم الحالي صاحب الطلب
        # افتح الصفحة إذا كانت القيمة هي True
        # وإلا فلا تفتحها؛ لأن هذا يعني المشروع ليس للمستخدم الحالي
        return self.get_object().project.user_id == self.request.user.id