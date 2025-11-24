import sys
from redis import Redis
from rq.worker import Worker, SimpleWorker
from app.core.rq_config import get_redis

if __name__ == "__main__":
    redis_conn = get_redis()

    if sys.platform.startswith("win"):
        # Windows — используем SimpleWorker
        worker = SimpleWorker(["moderation"], connection=redis_conn)
        print("Запущен SimpleWorker (Windows режим)")
    else:
        # Linux/macOS — обычный Worker
        worker = Worker(["moderation"], connection=redis_conn)
        print("Запущен Worker (Linux/macOS режим)")

    worker.work()
