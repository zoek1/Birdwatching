from celery import Celery
from os import environ

REDIS_URI = environ.get("QUEUE_REDIS_URI", "127.0.0.1")
REDIS_PORT = environ.get("QUEUE_REDIS_PORT", "6379" )
REDIS_DB = environ.get("QUEUE_REDIS_DB", "0")

app = Celery("tasks", broker=f"redis://{REDIS_URI}:{REDIS_PORT}/{REDIS_DB}")

@app.task
def run_task(*args, **kwargs):
  print('Hola desde el worker')
