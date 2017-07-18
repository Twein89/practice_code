# import socket

# sock = socket.socket()
# sock.setblocking(False)
# try:
#     sock.connect(('xkcd.com', 80))
# except BlockingIOError:
#     pass

# request = 'GET /353/ HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'
# encoded = request.encode('ascii')

# while True:
#     try:
#         sock.send(encoded)
#         break
#     except OSError as e:
#         pass

# print('sent')




import socket
from selectors import DefaultSelector, EVENT_WRITE

selector = DefaultSelector()

sock = socket.socket()
sock.setblocking(False)
try:
    sock.connect(('xkcd.com', 80))
except BlockingIOError:
    pass

def connected():
    selector.unregister(sock.fileno())
    print('connected!')
    return 'whooo!'

selector.register(sock.fileno(), EVENT_WRITE, connected)

def loop():
    while True:
        events = selector.select()
        for event_key, event_mask in events:
            print(event_key)
            callback = event_key.data
            print(callback())

loop()