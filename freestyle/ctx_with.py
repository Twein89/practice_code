from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        self.connections.append(self.sock)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()

from functools import partial
conn = LazyConnection(('www.python.org', 80))

# with conn as s:
#     s.send(b'GET /index.html HTTP/1.0\r\n')
#     s.send(b'Host: www.python.org\r\n')
#     s.send(b'\r\n')
#     resp = b''.join(iter(partial(s.recv, 8192), b''))
#     print(resp)
with conn as s1:
    pass
    with conn as s2:
        pass
