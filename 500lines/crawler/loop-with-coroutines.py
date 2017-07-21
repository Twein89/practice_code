from selectors import *
import socket
import re
import urllib.parse
import time

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

	