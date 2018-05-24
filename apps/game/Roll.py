import random

class Roll:

    @staticmethod
    def chance(num):
        return random.uniform(0, 1) < num
