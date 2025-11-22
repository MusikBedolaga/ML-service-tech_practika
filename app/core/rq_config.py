from redis import Redis
from rq import Queue
from functools import lru_cache

@lru_cache
def get_redis() -> Redis:
  return Redis(host="localhost", port=6379, db=0) # надо будет изменить

@lru_cache
def get_moderation_queue() -> Queue:
  redis_conn = get_redis()
  return Queue("moderation", connection=redis_conn)