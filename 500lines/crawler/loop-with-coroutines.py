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

def fetch(self):
	sock = socket.socket()
	sock.setblocking(False)
	try:
		sock.connect(('xkcd.com', 80))
	except BlockingIOError:
		pass

	f = Future()

	def on_connected():
		f.set_result(None)

	selector.register(sock.fileno(),
					  EVENT_WRITE,
					  on_connected)
	yield f
	selector.unregister(sock.fileno())
	print('connected!')


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

fetcher = Fetcher('/353/')
Task(fetcher.fetch())

loop()
