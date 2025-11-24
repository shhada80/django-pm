FROM python:3.11-slim

WORKDIR /app

# نسخ المتطلبات وتثبيتها
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# نسخ ملفات المشروع
COPY . .

# جمع الملفات الثابتة
RUN python manage.py collectstatic --noinput --clear

# المنفذ
EXPOSE 8000

# تشغيل المشروع باستخدام Gunicorn مع 3 workers
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "projects_management.wsgi:application"]
