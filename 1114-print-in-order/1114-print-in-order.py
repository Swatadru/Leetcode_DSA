import threading

class Foo:
    def __init__(self):
        self.second_semaphore = threading.Semaphore(0)
        self.third_semaphore = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_semaphore.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.second_semaphore.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_semaphore.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.third_semaphore.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()