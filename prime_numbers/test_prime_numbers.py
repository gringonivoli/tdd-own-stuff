from prime_numbers import PrimeNumbers


def test_prime_numbers():
    prime_numbers = PrimeNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    assert prime_numbers


def test_prime_numbers_is_empty():
    expected_value = []
    prime_numbers = PrimeNumbers([])

    result = [prime_number for prime_number in prime_numbers]

    assert result == expected_value


def test_prime_numbers_is_a_list_of_prime_numbers():
    expected_value = [1, 2, 3, 5, 7, 13, 11]
    prime_numbers = PrimeNumbers([1, 2, 3, 4, 5, 6, 8, 7, 13, 11, 20, 21])

    result = [prime_number for prime_number in prime_numbers]

    assert result == expected_value
