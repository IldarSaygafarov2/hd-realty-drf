FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8002

# CMD ["gunicorn", "--reload", "-c", "gunicorn_conf.py", "core.project.wsgi:application"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]