
from Code.Char_Frequency import count_frequency

def test_character_a():
    assert count_frequency("banana", "a") == 3

def test_character_n():
    assert count_frequency("banana", "n") == 2

def test_character_b():
    assert count_frequency("banana", "b") == 1

def test_character_not_present():
    assert count_frequency("hello", "z") == 0

def test_empty_string():
    assert count_frequency("", "a") == 0

def test_repeated_character():
    assert count_frequency("aaaa", "a") == 4
