import random
class Dice:
    def __init__(self,arr):
        self.arr = arr
    def roll(self):
        for i in range(1000):
            self.arr.append(random.randint(1,6))
