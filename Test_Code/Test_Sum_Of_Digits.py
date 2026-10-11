
from Code.Sum_Of_Digits import sum_of_digits

def test_sum_of_digits():
    assert sum_of_digits(123) == 6

def test_single_digit():
    assert sum_of_digits(5) == 5

def test_zero():
    assert sum_of_digits(0) == 0

def test_large_number():
    assert sum_of_digits(12345) == 15

def test_negative_number():
    assert sum_of_digits(-123) == 6
