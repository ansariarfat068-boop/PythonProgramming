from Code.Missing_Number import find_missing


def test_missing_number():
    assert find_missing([1, 2, 4, 5]) == 3


def test_missing_first():
    assert find_missing([2, 3, 4]) == 1


def test_missing_last():
    assert find_missing([1, 2, 3]) == 4
