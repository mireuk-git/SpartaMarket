# Dockerfile
FROM python:3.12

# 작업 디렉토리 설정
WORKDIR /app

#의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 복사
COPY . .

# 포트 노출
EXPOSE 8000

# 서버 실행
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
