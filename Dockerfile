FROM python:3.11-slim

WORKDIR /app

# تثبيت المتطلبات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ كل الملفات
COPY . .

# جمع الملفات الثابتة
RUN python manage.py collectstatic --noinput --clear

# المنفذ
EXPOSE 8000

# تشغيل gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "projects_management.wsgi:application"]