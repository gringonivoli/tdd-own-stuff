class Int(int):

    def is_prime(self):
        result = False if self <= 1 else True
        for number in range(1, self):
            if number != 1 and number != self and self % number == 0:
                result = False
                break

        return result
