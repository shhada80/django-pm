# من خلال هذا الملف يمكننا عمل ضبط للوحة التحكم لهذا التطبيق

from django.contrib import admin
from . import models

# Register your models here.
# تسجيل النماذج التي نرغب بإدارتها

# من خلال admin يمكن عمل register للنموذج Category
admin.site.register(models.Category)
# تسجيل نموذج المشروع Project
admin.site.register(models.Project)
# تسجيل نموذج المهمة Task
admin.site.register(models.Task)
