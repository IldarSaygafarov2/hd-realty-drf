from celery import Celery
import os
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.project.settings")

app = Celery("hd_realty_drf")

app.conf.beat_schedule = {
    "get-currency-rate-every-day-at-9": {
        "task": "core.apps.advertisements.tasks.get_todays_currency_rate",
        "schedule": crontab(hour=9, minute=0),
    },
}

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
