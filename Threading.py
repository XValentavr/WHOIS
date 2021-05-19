import queue
import threading
import time
from Domains import create_domain


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print('Starting thread %s.' % self.name)
        process_queue()
        print('Exiting thread %s.' % self.name)


def process_queue():
    while True:
        try:
            x = my_queue.get(block=False)
        except queue.Empty:
            return
        else:
            print_factors(x)

        time.sleep(1)


def print_factors(x):
    create_domain(x)


input_ = ['.com', '.org', '.biz', '.net', '.info']
my_queue = queue.Queue()
for x in input_:
    my_queue.put(x)

thread1 = MyThread('1')
thread2 = MyThread('2')
thread3 = MyThread('3')
thread4 = MyThread('4')
thread5 = MyThread('5')

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

