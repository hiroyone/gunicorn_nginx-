# The official documents
# https://github.com/benoitc/gunicorn
import multiprocessing
import os

# Worker Processes
workers = 4
worker_class = 'sync'

# Logging
HOME=os.environ['HOME']
logfile = './gunicorn_nginx/app.log'
loglevel = 'info'
logconfig = None

# Localhost binding
bind = '127.0.0.1:8000'
# Max nums of pending connections
backlog = 2048
# Max clients a process can handle
worker_connections = 1000
# Connection Timeout
timeout = 30
# The number of seconds to wait for the next request on a Keep-Alive HTTP connection.
keepalive = 2

# Socket communication
socket_path = 'unix:/tmp/myapp-api.sock'
bind = socket_path

