from django.db import models
# نموذج User يقدمه لنا جانغو ضمنياً؛ لتمثيل العلاقة بين المستخدم والمشروع
from django.conf.global_settings import AUTH_USER_MODEL
# خاص بتعريب العبارات
from django.utils.translation import gettext as _

# Create your models here.

# التصنيف
# نعرف صنفاً جديداً خاص بكيان التصنيف
class Category(models.Model):
    # حقول النموذج
    # اسم التصنيف
    name = models.CharField(max_length=255)

    # ستعيد لنا نتيجة عند تحويل الصنف إلى سلسلة نصية
    def __str__(self):
        return self.name

    class Meta:
        # صنف فرعي نحدد فيه بعض الخصائص لهذه النماذج، وهذا مفيد لتعريبها؛ كي تظهر معربة في لوحة التحكم
        verbose_name = _('Category') # الاسم في حالة المفرد
        verbose_name_plural = _('Category') # الاسم في حالة الجمع، وبدون هذا السطر سيظهر حرف s بجانب الاسم


# نموذج مساعد للمشروع خاص بحالة المشروع
"""
هذا النموذج لا يرث من Model بل يرث من صنف آخر يدعى IntegerChoices
وبالتالي فهو عبارة عن نموذج مساعد لتمثيل حالة المشروع
"""
class ProjectStatus(models.IntegerChoices):
    # سنستخدم ضمنه حقول الخيارات ل
    # تعريف الحالات الموجودة لدينا
    """
    PENDING = 1, 'Pending'
    Pending القيمة التي ستظهر للمستخدم عند تمثيل المشروع في الواجهة
    بينما القيمة 1 هي التي ستخزن في قاعدة البيانات
    أما كلمة PENDING يمكن استخدامها ضمن الشيفرة بدلاً من الرقم 1 للوضوح وتجنب الأخطاء
    """
    # PENDING = 1, 'Pending' # قيد التنفيذ
    # COMPLETED = 2, 'Completed' # مكتمل
    # POSTPONED = 3, 'Postponed' # مؤجل
    # CANCELLED = 4, 'Cancelled' # ملغي

    # # ترجمة حالة المشروع
    PENDING = 1, _('Pending') # قيد التنفيذ
    COMPLETED = 2, _('Completed')  # مكتمل
    POSTPONED = 3, _('Postponed') # مؤجل
    CANCELED = 4, _('Canceled') # ملغي



# المشروع
class Project(models.Model):
    # خواص المشروع
    # عنوان المشروع
    title = models.CharField(max_length=255)
    # وصف المشروع
    description = models.TextField()
    # إنشاء حقل يعبر عن الحالة من النوع Integer
    # الخيارات المتاحة لهذا الحقل هي الخيارات من الصنف ProjectStatus الموجود في الأعلى
    status = models.IntegerField(
        choices=ProjectStatus.choices, # type: ignore
        # في السطر السابق كتبنا: type: ignore؛ السبب: PyCharm أحياناً لا يتعرف تلقائياً على الخصائص الديناميكية التي ينشئها IntegerChoices
        # الحالة الافتراضية: قيد التنفيذ
        default=ProjectStatus.PENDING
    )
    # تاريخ الإنشاء
    create_at = models.DateTimeField(auto_now_add=True) # auto_now_add: يضبط التاريخ عند الإنشاء فقط (مرة واحدة)
    # تاريخ التعديل
    update_at = models.DateTimeField(auto_now=True) # auto_now: يحدث التاريخ تلقائياً عند كل تعديل على النموذج

    # تمثيل حقول العلاقات
    # العلاقة بين النموذج Category والمشروع
    # نوع العلاقة: واحد إلى كثير
    # PROTECT: يمنع حذف التصنيف إذا كانت هناك مشروع مرتبط به
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # العلاقة بين النموذج User والمشروع
    # نوع العلاقة: واحد إلى كثير
    # CASCADE: عند حذف المستخدم، تُحذف كل المشاريع المرتبطة به تلقائياً
    """
    لم ننشئ النموذج User بعد، ولسنا بحاجة لذلك فعلياً؛ حيث يقدم لنا جانغو هذا النموذج بشكل ضمني
    وهو AUTH_USER_MODEL، ويمكن استخدامه هنا لتمثيل هذه العلاقة، وذلك بعد استيراده في الأعلى
    """
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        # تعني أن الحقل يمكن أن يكون فارغاً
        null=True
    )


    # لتمثيل الكائن بسلسلة نصية، وهي العنوان
    def __str__(self):
        return self.title

    class Meta:
        # صنف فرعي نحدد فيه بعض الخصائص لهذه النماذج، وهذا مفيد لتعريبها؛ كي تظهر معربة في لوحة التحكم
        verbose_name = _('Projects')  # الاسم في حالة المفرد
        verbose_name_plural = _('Project') # الاسم في حالة الجمع، وبدون هذا السطر سيظهر حرف s بجانب الاسم


# المهمة
class Task(models.Model):
    # خواص المهمة
    # وصف المهمة
    description = models.TextField()
    # حالة المهمة: مكتملة أم لا؟
    is_completed = models.BooleanField(default=False) # False: غير مكتملة، وعند إضافة مهمة تكون غير مكتملة بعد
    # تمثيل حقول العلاقات
    # العلاقة بين النموذج Project والمهام
    # نوع العلاقة: واحد إلى كثير
    # CASCADE: عند حذف المشروع، تُحذف كل المهام المرتبطة به تلقائياً
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # لتمثيل الكائن بسلسلة نصية، وهي الوصف
    def __str__(self):
        return self.description

    class Meta:
        # صنف فرعي نحدد فيه بعض الخصائص لهذه النماذج، وهذا مفيد لتعريبها؛ كي تظهر معربة في لوحة التحكم
        verbose_name = _('Task') # الاسم في حالة المفرد
        verbose_name_plural = _('Task') # الاسم في حالة الجمع، وبدون هذا السطر سيظهر حرف s بجانب الاسم