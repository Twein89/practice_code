import tornado.ioloop

#1.tornado.ioloop.IOLoop.instance().start()
#2. ...stop()

#3.ioloop.IOLoop.current()

#4.io_loop.run_sync(func, time=None)

# def func():
#     print("hello world")
#
# io_loop = tornado.ioloop.IOLoop.instance()
# io_loop.run_sync(func)

#start, func, stop

#5.add_handler(fd, handler, events) IOLoop.READ, WRITE, ERROR sock.fileno()
#fd: 所监听的socket的文件描述符

#6.update_handler(fd, events)

#7.remove_handler(fd)

#1.add_callback(cb, *args, **kw)
# io_loop = tornado.ioloop.IOLoop.instance()
# io_loop.add_callback(func)
# io_loop.start()

#2.add_callback_fromsignal(cb, *args, **kw)

#3.add_future(future, callback)
#4.add_timeout(deadline, callback, *args, **kw)
# remove_timeout()
#5.call_later(delay, callback, *args, **kw)

# io_loop.call_later(5, func)
# io_loop.call_at(time, func)

#spawn_callback(cb, *args, **kw)
#io_loop.time()

def func(a):
    print(a)

def func2():
    print(io_loop.time())

io_loop = tornado.ioloop.IOLoop.instance()

io_loop.add_callback(func, 1)
io_loop.call_later(5, func2)

io_loop.start()
