import multiprocessing
import os

name = 'gunicorn'

accesslog = 'accesslog.log'
errorlog = 'errorlog.log'

bind = '0.0.0.0:8080'

worker_class = "uvicorn.workers.UvicornWorker"
workers = multiprocessing.cpu_count() * 2 + 1
worker_connection = '1024'
backlog = 2048
max_requests = 5120
timeout = 120
keepalive = 2

user = os.environ.get('PYUSER')
group = os.environ.get('PYGROUP')

debug = os.environ.get('DEBUG', 'false') == 'true'
reload = debug
preload_app = False
daemon = False
