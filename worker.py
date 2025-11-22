from redis import Redis
from rq import Queue, Worker

redis_conn = Redis(host="localhost", port=6379, db=0)

if __name__ == "__main__":
    queue = Queue("moderation", connection=redis_conn)

    # Воркера явно привязываем к этому же соединению Redis
    worker = Worker([queue], connection=redis_conn)

    # Запускаем воркера: он будет слушать очередь и выполнять задачи
    worker.work()
