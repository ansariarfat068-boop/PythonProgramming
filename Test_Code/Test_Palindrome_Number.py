

from Code.Check_Palindrome_Number import check_palindrome

def test_palindrome_121():
    assert check_palindrome(121) == "PALINDROME"

def test_not_palindrome_123():
    assert check_palindrome(123) == "NOT PALINDROME"

def test_palindrome_1221():
    assert check_palindrome(1221) == "PALINDROME"

def test_palindrome_7():
    assert check_palindrome(7) == "PALINDROME"

def test_not_palindrome_10():
    assert check_palindrome(10) == "NOT PALINDROME"

