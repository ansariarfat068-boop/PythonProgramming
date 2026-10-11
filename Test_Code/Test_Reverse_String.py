
from Code.Reverse_String import reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_reverse_word():
    assert reverse_string("python") == "nohtyp"

def test_single_character():
    assert reverse_string("A") == "A"

def test_empty_string():
    assert reverse_string("") == ""

def test_palindrome():
    assert reverse_string("madam") == "madam"

def test_string_with_numbers():
    assert reverse_string("abc123") == "321cba"
