@echo on
call .venv\Scripts\activate
start cmd /k uvicorn api.main:app --port 8000
start cmd /k celery -A api.tasks.celery_conf:celery worker --loglevel=INFO --pool=solo