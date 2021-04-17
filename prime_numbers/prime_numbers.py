from typing import List
from prime_numbers.int import Int


class PrimeNumbers:

    def __init__(self, numbers: List[int]):
        self._numbers = numbers

    def __iter__(self):
        for number in self._numbers:
            if Int(number).prime():
                yield number
