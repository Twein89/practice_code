from multiprocessing.connection import Listener
from threading import Thread

def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

from rpcserver import RPCHandler

handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)

rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')
