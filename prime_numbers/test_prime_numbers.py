from prime_numbers.prime_numbers import PrimeNumbers


def test_prime_numbers():
    prime_numbers = PrimeNumbers([1, 2, 3, 4, 12, 13])

    assert prime_numbers is not None


def test_prime_numbers_is_empty_for_no_values():
    prime_numbers = PrimeNumbers([])

    assert list(prime_numbers) == []


def test_prime_numbers_is_empty_for_no_prime_numbers():
    prime_numbers = PrimeNumbers([4, 6, 8, 10])

    assert list(prime_numbers) == []


def test_prime_numbers_is_a_iterable_of_prime_numbers():
    expected_value = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    prime_numbers = PrimeNumbers(list(range(1, 100)))

    assert list(prime_numbers) == expected_value
