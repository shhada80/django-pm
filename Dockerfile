FROM python:3.11-slim

# تثبيت Nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# نسخ وتثبيت المتطلبات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ المشروع
COPY . .

# جمع الملفات الثابتة
RUN python manage.py collectstatic --noinput --clear

# إعداد Nginx
RUN echo 'server {\n\
    listen 8000;\n\
    server_name _;\n\
\n\
    location /static/ {\n\
        alias /app/staticfiles/;\n\
        expires 30d;\n\
        add_header Cache-Control "public, immutable";\n\
    }\n\
\n\
    location / {\n\
        proxy_pass http://127.0.0.1:8001;\n\
        proxy_set_header Host $host;\n\
        proxy_set_header X-Real-IP $remote_addr;\n\
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;\n\
        proxy_set_header X-Forwarded-Proto $scheme;\n\
    }\n\
}\n' > /etc/nginx/sites-available/default

# سكريبت التشغيل
RUN echo '#!/bin/bash\n\
nginx\n\
gunicorn --bind 127.0.0.1:8001 --workers 3 projects_management.wsgi:application\n' > /start.sh && chmod +x /start.sh

EXPOSE 8000

CMD ["/start.sh"]