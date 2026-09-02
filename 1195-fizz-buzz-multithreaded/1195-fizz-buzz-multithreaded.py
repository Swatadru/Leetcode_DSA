from threading import Condition

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.cur = 1                 # index currently being printed (1-indexed)
        self.cv = Condition()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        with self.cv:
            while True:
                while self.cur <= self.n and not (self.cur % 3 == 0 and self.cur % 5 != 0):
                    self.cv.wait()
                if self.cur > self.n:
                    self.cv.notify_all(); return
                printFizz()
                self.cur += 1
                self.cv.notify_all()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        with self.cv:
            while True:
                while self.cur <= self.n and not (self.cur % 5 == 0 and self.cur % 3 != 0):
                    self.cv.wait()
                if self.cur > self.n:
                    self.cv.notify_all(); return
                printBuzz()
                self.cur += 1
                self.cv.notify_all()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        with self.cv:
            while True:
                while self.cur <= self.n and self.cur % 15 != 0:
                    self.cv.wait()
                if self.cur > self.n:
                    self.cv.notify_all(); return
                printFizzBuzz()
                self.cur += 1
                self.cv.notify_all()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        with self.cv:
            while True:
                while self.cur <= self.n and (self.cur % 3 == 0 or self.cur % 5 == 0):
                    self.cv.wait()
                if self.cur > self.n:
                    self.cv.notify_all(); return
                printNumber(self.cur)
                self.cur += 1
                self.cv.notify_all()