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

host_url = 'www.xinhuanet.com'



class Fetcher:
    def __init__(self, url):
        self.response = b''
        self.url = url
        self.sock = None

    def fetch(self):
        global concurrency_achieved
        concurrency_achieved = max(concurrency_achieved, len(urls_todo))
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect((host_url, 80))
        except BlockingIOError:
            pass

        # Register next callback
        selector.register(self.sock.fileno(),
                          EVENT_WRITE,
                          self.connected)

    def connected(self, key, mask):
        print('connected!')
        selector.unregister(key.fd)
        # request = 'GET {} HTTP/1.0\r\nHost: hz.ganji.com\r\n\r\n'.format(self.url)
        # request = 'GET {} HTTP/1.0\r\nHost: ganji.com\r\n\r\n'.format(self.url, host)
        # request = 'GET {} HTTP/1.0\r\n\r\n'.format(self.url, host)
        request = 'GET {} HTTP/1.0\r\n'.format(self.url)
        request += 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36\r\n'
        request += 'Accept: */*\r\n'
        request += 'Host: {}\r\n\r\n'.format(host_url)
        # print(request)
        self.sock.send(request.encode('ascii'))

        # Register next callback
        selector.register(key.fd,
                          EVENT_READ,
                          self.read_response)

    def read_response(self, key, mask):
        global stopped
        try:
            chunk = self.sock.recv(4096)
        except:
            return
        if chunk:
            self.response += chunk
            # print(self.response)
        else:
            selector.unregister(key.fd)
            links = self.parse_links()

            # Python set-logic
            for link in links.difference(seen_urls):
                urls_todo.add(link)
                # print(link)
                Fetcher(link).fetch()  # <- New Fetcher.

            seen_urls.update(links)
            urls_todo.remove(self.url)
            if not urls_todo:
                stopped = True
            print(self.url)

    def body(self):
        body = self.response.split(b'\r\n\r\n', 1)[1]
        return body.decode('utf-8')

    def parse_links(self):
        if not self.response:
            print('error: {}'.format(self.url))
            return set()
        if not self._is_html():
            return set()

        urls = set(re.findall(r'''(?i)href=["']?([^\s"'<>]+)''', self.body()))
        links = set()
        for url in urls:
            normalized = urllib.parse.urljoin(self.url, url)
            parts = urllib.parse.urlparse(normalized)
            if parts.scheme not in ('', 'http', 'https'):
                continue
            # if host and host.lower() not in ('xkcd.com', 'www.xkcd.com'):
            host, port = urllib.parse.splitport(parts.netloc)
            if host and host.lower() not in ('xinhuanet.com', 'www.xinhuanet.com'):
                continue
            defragmented, frag = urllib.parse.urldefrag(parts.path)
            links.add(defragmented)

        return links

    def _is_html(self):
        head, body = self.response.split(b'\r\n\r\n', 1)
        headers = dict(h.split(': ') for h in head.decode().split('\r\n')[1:])
        return headers.get('Content-Type', '').startswith('text/html')

start = time.time()
fetcher = Fetcher('/')
fetcher.fetch()

while not stopped:
    events = selector.select()
    for event_key, event_mask in events:
        callback = event_key.data
        callback(event_key, event_mask)

print('{} URLs fetched in {:.1f} seconds, achieved concurrency = {}'.format(
    len(seen_urls), time.time() - start, concurrency_achieved))
            