from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserRegisterForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# استمارة تسجيل الدخول
class RegisterView(CreateView):
    form_class = UserRegisterForm
    # رابط إعادة التوجيه
    # إذا أردنا إعادة توجيهه لصفحة تسجيل الدخول
    # success_url = reverse_lazy('login')
    # اسم القالب
    template_name = 'registration/register.html'

    # سنقوم بعملية تسجيل الدخول بشكل تلقائي بعد نجاح عملية التسجيل
    def get_success_url(self):
        login(self.request, self.object)
        # إعادة توجيه لصفحة قائمة المشاريع
        return reverse_lazy('Project_list')


# فائدة هذا المزخرف أنه سيعدينا لصفحة تسجيل الدخول عندما نذهب لصفحة الملف الشخصي عندما نكون مسجلي الخروج
# وبدونه ستظهر لنا صفحة خطأ
@login_required
def edit_profile(request):
    if request.method == 'POST':
        # حفظ التغييرات إذا كان الطلب من النوع POST وذلك عندما يعدل المستخدم بيانات ملفه الشخصي
        # تحديد الاستمارة، وتمرير كائن المستخدم إليها
        form = ProfileForm(request.POST, instance=request.user)
        # التأكد من أن الاستمارة صالحة
        if form.is_valid():
            # حفظ التغييرات
            form.save()
            # إعادة التوجيه
            # إعادة القالب وتمرير الاستمارة
            return redirect('profile')
    else:
        # تحديد الاستمارة، وتمرير كائن المستخدم إليها
        form = ProfileForm(instance=request.user)
        # إعادة القالب وتمرير الاستمارة
        return render(request, 'profile.html', {
            'form': form
        })