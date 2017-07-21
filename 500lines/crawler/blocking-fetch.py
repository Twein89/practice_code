import socket


host = 'www.xinhuanet.com'
def fetch(url):
    sock = socket.socket()
    sock.connect((host, 80))
    # request = "GET {} HTTP/1.1\r\nHost: {}\r\n\r\n".format(url, host)
    request = 'GET {} HTTP/1.0\r\nHost: {}\r\n\r\n'.format(url, host)
    # request = 'GET / HTTP/1.0\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    print(response.decode('utf-8'))

fetch('/politics/')

# host = 'www.4399.com'
# import socket
# def fetch(link):
#     sock = socket.socket()
#     sock.connect((host,80))
#     request = 'GET {} HTTP/1.0\r\nHost: {}\r\n\r\n'.format(link, host)
#     sock.send(request.encode('ascii'))
#     response = b''
#     chunk = sock.recv(4096)
#     while chunk:
#         response += chunk
#         chunk = sock.recv(4096)
#     print(response)
# fetch('/')