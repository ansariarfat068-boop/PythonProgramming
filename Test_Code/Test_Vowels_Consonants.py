
from Code.Vowels_Consonants import check_vowel_consonant

def test_vowel_a():
    assert check_vowel_consonant("a") == "Vowel"

def test_vowel_e():
    assert check_vowel_consonant("E") == "Vowel"

def test_consonant_b():
    assert check_vowel_consonant("b") == "Consonant"

def test_consonant_z():
    assert check_vowel_consonant("z") == "Consonant"

def test_invalid_number():
    assert check_vowel_consonant("5") == "Invalid"

def test_invalid_empty():
    assert check_vowel_consonant("") == "Invalid"
