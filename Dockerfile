# Python base
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安裝依賴套件
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd  \
    && rm -rf /var/lib/apt/lists/*

# 建立目錄並複製專案檔案
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# 預設啟動指令
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
