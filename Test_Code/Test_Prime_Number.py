
from Code.Prime_Number import check_prime

def test_prime_7():
    assert check_prime(7) == "PRIME"

def test_prime_29():
    assert check_prime(29) == "PRIME"

def test_not_prime_6():
    assert check_prime(6) == "NOT PRIME"

def test_not_prime_18():
    assert check_prime(18) == "NOT PRIME"

def test_not_prime_1():
    assert check_prime(1) == "NOT PRIME"

