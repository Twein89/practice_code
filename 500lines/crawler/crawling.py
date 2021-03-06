try:
    from asyncio import JoinableQueue as Queue
except ImportError
    from asyncio import Queue

loop = asyncio.get_event_loop()

crawler = crawling.Crawler('http://xkcd.com', max_redirect=10)

loop.run_until_complete(crawler.crawl())

class Crawler:

    def __init__(self, root_url, max_redirect):
        self.max_tasks = 10
        self.max_redirect = max_redirect
        self.q = Queue()
        self.seen_urls = set()

        self.session = aiohttp.ClientSession(loop=loop)
        self.q.put((root_url, self.max_redirect))

    @asyncio.coroutine
    def crawl(self):
        """Run the crawler until all work is done"""
        workers = [asyncio.Task(self.work())
                   for _ in range(self.max_tasks)]

        # When all work is done, exit
        yield from self.q.join()
        for w in workers:
            w.cancel()
