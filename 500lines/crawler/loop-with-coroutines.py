from selectors import *
import socket
import re
import urllib.parse
import time

urls_todo = set(['/'])
seen_urls = set(['/'])
concurrency_achieved = 0
selector = DefaultSelector()
stopped = False


host_url = 'www.xinhuanet.com'

class Future:

    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)

    def __iter__(self):
        yield self
        return self.result

class Fetcher:

    def __init__(self, url):
        self.response = b''
        self.url = url
        self.sock = None

    def fetch(self):
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect((host_url, 80))
        except BlockingIOError:
            pass

        # f = Future()

        # def on_connected():
        #     f.set_result(None)

        # selector.register(sock.fileno(),
        #                   EVENT_WRITE,
        #                   on_connected)
        # yield f
        # selector.unregister(sock.fileno())
        # print('connected!')

        # print(request)

        request = 'GET {} HTTP/1.0\r\n'.format(self.url)
        request += 'Host: {}\r\n\r\n'.format(host_url)
        sock.send(request.encode('ascii'))
        sock.response = yield from read_all(sock)


    def read(sock):
        f = Future()

        def on_readable():
            f.set_result(sock.recv(4096))

        selector.register(sock.fileno(), EVENT_READ, on_readable)
        chunk = yield f
        selector.unregister(sock.fileno())
        return chunk


    def read_all(sock):
        response = []
        chunk = yield from read(sock)
        while chunk:
            response.append(chunk)
            chunk = yield from read(sock)

        return b''.join(response)


class Task:
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try: 
            next_future = self.coro.send(future.result)
        except StopIteration:
            return

        next_future.add_done_callback(self.step)


def loop():
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()

fetcher = Fetcher('/')
Task(fetcher.fetch())

loop()
