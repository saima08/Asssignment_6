class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.n = self.start
        return self

    def __next__(self):
        if self.n < 0:
            raise StopIteration
        current = self.n
        self.n -= 1
        return current

for i in Countdown(5):
    print(i)
