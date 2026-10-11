
from Code.Second_Largest import second_largest

def test_second_largest():
    assert second_largest([10, 20, 30, 40, 50]) == 40

def test_unsorted_list():
    assert second_largest([5, 1, 9, 3, 7]) == 7

def test_duplicate_numbers():
    assert second_largest([10, 10, 8, 5]) == 8

def test_negative_numbers():
    assert second_largest([-10, -5, -2, -8]) == -5

def test_two_numbers():
    assert second_largest([10, 20]) == 10

def test_same_numbers():
    assert second_largest([5, 5, 5]) is None
