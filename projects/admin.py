# من خلال هذا الملف يمكننا عمل ضبط للوحة التحكم لهذا التطبيق

from django.contrib import admin
from django.db.models import Count
from . import models

# Register your models here.
# تسجيل النماذج التي نرغب بإدارتها

# من خلال admin يمكن عمل register للنموذج Category
admin.site.register(models.Category)
# # تسجيل نموذج المشروع Project
# admin.site.register(models.Project)
# # تسجيل نموذج المهمة Task
# admin.site.register(models.Task)

# تغيير طريقة التسجيل إلى الشكل الآتي:
# تخصيص واجهة المشاريع
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    # الأعمدة المطلوبة
    list_display = ['title', 'status', 'user', 'category', 'create_at', 'tasks_count']
    # عدد السجلات في كل صفحة
    list_per_page = 20
    # الأعمدة القابلة للتعديل
    list_editable = ['status']
    # تفادي كثرة الاستعلامات
    # ضمنه نحدد العلاقات التي نرغب بتحميلها
    list_select_related = ['category', 'user']

    # توفير خاصية لـ tasks_count
    # اسم الدالة يجب أن يكون كاسم الخاصية الموجودة ضمن list_display
    def tasks_count(self, obj):
        # return obj.task_set.count()
        # عدد مهام كل مشروع
        return obj.tasks_count

    # تخصيص الاستعلام لتفادي كثرة الاستعلامات
    # جلب عدد المهام سيؤدي إلى استعلام لكل مهمة؛ لذا يجب تفادي ذلك
    def get_queryset(self, request):
        # استدعاء الدالة من الصنف الأب
        query = super().get_queryset(request)
        # تخصيص الاستعلام لإضافة خاصية جديدة تدعى tasks_count
        query = query.annotate(tasks_count=Count('task'))
        return query


# تخصيص واجهة عرض المهام
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    # الأعمدة المطلوبة
    list_display = ['id', 'description', 'project', 'is_completed']
    # الأعمدة القابلة للتعديل
    list_editable = ['is_completed']
    # عدد السجلات في كل صفحة
    list_per_page = 20
