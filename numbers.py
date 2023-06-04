import random

class Numbers:
    def __init__(self):
        self.numbers = [random.randint(1, 100) for i in range(10)]

    def summa(self):
        return sum(self.numbers)

    def average(self):
        return sum(self.numbers) / len(self.numbers)

    def maximum(self):
        return max(self.numbers)

    def minimum(self):
        return min(self.numbers)
