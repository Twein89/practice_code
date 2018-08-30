import asyncio
import requests
import time

def sleep(x):
    time.sleep(x)
    return 'sleep {} seconds'.format(x)

@asyncio.coroutine
def main():
    loop = asyncio.get_event_loop()
#    future1 = loop.run_in_executor(None, requests.get, 'http://www.baidu.com')
#    future2 = loop.run_in_executor(None, requests.get, 'http://www.163.com')
    future1 = loop.run_in_executor(None, sleep, 9)
    future2 = loop.run_in_executor(None, sleep, 12)
    response1 = yield from future1
    response2 = yield from future2
    print(response1)
    print(response2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
