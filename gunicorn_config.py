import time

bind = '0.0.0.0:8083'
workers = 1
loglevel = "info"


def pre_request(worker, req):
    req.start_time = time.time()
    worker.log.info(f"[START] {req.method} {req.path} from {req.remote_addr}")


def post_request(worker, req, environ, resp):
    duration = time.time() - getattr(req, 'start_time', time.time())
    worker.log.info(f"[END] {req.method} {req.path} → {resp.status} in {duration:.3f}s")


def worker_abort(worker):
    worker.log.info("Aborted for timeout!")
    raise TimeoutError('Request timed out')


pre_request = pre_request
post_request = post_request
worker_abort = worker_abort

timeout = 99999
keepalive = 2

max_requests = 20000
