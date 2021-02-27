from typing import List


class PrimeNumbers:

    def __init__(self, numbers: List[int]):
        self._numbers = numbers

    def __iter__(self):
        for number in self._numbers:
            if self._is_prime(number):
                yield number

    @staticmethod
    def _is_prime(number):
        result = True
        for i in range(1, number):
            if i != 1 and i != number and number % i == 0:
                result = False
        return result
