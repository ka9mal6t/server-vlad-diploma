from celery import Celery

from api.config import REDIS_HOST

celery = Celery(
    "tasks",
    broker=REDIS_HOST,
    include=["api.tasks.tasks"],
)
