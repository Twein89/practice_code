import time

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

from threading import Thread

#t = Thread(target=countdown, args=(10,))
##t = Thread(target=countdown, args=(10,), daemon=True)
#t.start()
#
#t.join()
#
#if t.is_alive():
#    print('Still running')
#else:
#    print('Completed')

class CountdownTask:
    def __init__(self):
        self._runing = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._runing and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(1)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate()
t.join()
