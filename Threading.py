import threading
from queue import Queue
from Domains import create_domain


class Downloader(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            url = self.queue.get()

            self.download_info(url)

            self.queue.task_done()

    def download_info(self, url):
        create_domain(url)


def main(urls):
    queue = Queue()

    for i in range(len(urls)):
        t = Downloader(queue)
        t.setDaemon(True)
        t.start()

    for url in urls:
        queue.put(url)

    queue.join()


if __name__ == "__main__":
    urls = ['.com', '.org','.net', '.info']
    main(urls)
