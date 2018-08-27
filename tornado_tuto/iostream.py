#1.io_loop
#2.max_buffer_size:最大可接受数据的大小，默认是100m
#3.read_trunk_size: read data 64k
#4.max_write_buffer_size write buff

#1.write(data, callback=None)

#2.read_bytes(num_bytes, cb=None, streaming_callback=None, partial=False)
#data
#return future
#streaming_callback

#3.read_until(delimiter, cb, max_bytes)

#4.read_until_close(cb, streaming_callback)

#5.close()

#6.set_close_callback(cb)

#7.closed()
#8.writing()
#9.reading()
#10. fileno()
#11. close_fd()

#12.write_to_fd(data) return write succ size
#13.read_from_fd()

#14. get_fd_error()

import tornado.ioloop
import tornado.iostream
import socket

def send_request():
    stream.write(b"GET / HTTP/1.0\r\nHost: baidu.com\r\n\r\n")
    stream.read_until(b"\r\n\r\n", on_headers)

def on_headers(data):
    headers = {}
    for line in data.split(b"\r\n"):
        parts = line.split(b":")
        if len(parts) == 2:
            headers[parts[0].strip()] = parts[1].strip()
    stream.read_bytes(int(headers[b"Content-Length"]), on_body)

def on_body(data):
    print(data)
    stream.close()
    tornado.ioloop.IOLoop.current().stop()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    stream = tornado.iostream.IOStream(s)
    stream.connect(('www.baidu.com', 80), send_request)
    tornado.ioloop.IOLoop.current().start()
