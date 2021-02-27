class Int(int):

    def is_prime(self):
        result = True
        for number in range(1, self):
            if number != 1 and number != self and self % number == 0:
                result = False
        return result
