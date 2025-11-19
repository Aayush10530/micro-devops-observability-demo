#!/usr/bin/env python3
import argparse
import logging
import socket
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
HOSTNAME = socket.gethostname()

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()

def run_http_server(port=8080):
    server = HTTPServer(("", port), HealthHandler)
    server.serve_forever()
def main(loop=True, interval=5):
    t = Thread(target=run_http_server, args=(8080,), daemon=True)
    t.start()

    if not loop:
        logging.info(f"Hello from {HOSTNAME}. Exiting.")
        return

    i = 0
    while True:
        logging.info({"msg": "hello", "host": HOSTNAME, "count": i})
        i += 1
        time.sleep(interval)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--once", action="store_true")
    p.add_argument("--interval", type=int, default=5)
    args = p.parse_args()
    main(loop=not args.once, interval=args.interval)

def main(loop=True, interval=5):
    t = Thread(target=run_http_server, args=(8080,), daemon=True)
    t.start()
    if not loop:
        logging.info(f"Hello from {HOSTNAME}. Exiting.")
        return
    i = 0
    while True:
        logging.info({"msg": "hello", "host": HOSTNAME, "count": i})
        i += 1
        time.sleep(interval)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--once", action="store_true")
    p.add_argument("--interval", type=int, default=5)
    args = p.parse_args()
    main(loop=not args.once, interval=args.interval)
