import os
from datetime import timedelta

from celery import Celery
from kombu import Exchange, Queue

app = Celery(__name__, include=['background.tasks'], )

app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/1")

providers_exchange = Exchange("providers_exchange", type="direct")  # External connections queue
internal_exchange = Exchange("steam_exchange", type="direct")  # internal queue

app.conf.task_queues = (
    Queue("base_steam_queue", providers_exchange, routing_key="items_base_route"),
    Queue("steam_queue", internal_exchange, routing_key="steam_route"),
)

app.conf.beat_schedule = {
    # Executes every 2 hours
    "parse": {
        "task": "background.tasks.parser.prepare_dota_tasks",
        "schedule": timedelta(seconds=10),
        'options': {
            'queue': 'steam_queue',
            # 'expires': timedelta(hours=2),
        },
    },
}
