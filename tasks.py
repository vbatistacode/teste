import time
import os

from celery import Celery

app = Celery()
app.conf.broker_url = os.getenv("CELERY_BROKER_URL")
app.conf.result_backend = os.getenv("CELERY_RESULT_BACKEND")

@app.task
def create_task(a,b,c):
    time.sleep(a)
    return b+c