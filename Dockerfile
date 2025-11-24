FROM python:3.11-slim

# تعيين متغير البيئة
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# نسخ وتثبيت المتطلبات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ جميع ملفات المشروع
COPY . .

# جمع الملفات الثابتة
RUN python manage.py collectstatic --noinput --clear

# المنفذ
EXPOSE 8000

# تشغيل التطبيق
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120", "projects_management.wsgi:application"]