class Int(int):

    def is_prime(self):
        result = True
        if self == 1:
            result = False
        else:
            for number in range(1, self):
                if number != 1 and number != self and self % number == 0:
                    result = False
                    break
        return result
