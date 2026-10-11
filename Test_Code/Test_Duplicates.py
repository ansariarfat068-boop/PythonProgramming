
from Code.Find_Duplicates import find_duplicates


def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2, 4, 3]) == [2, 3]


def test_no_duplicates():
    assert find_duplicates([1, 2, 3, 4]) == []


def test_empty_list():
    assert find_duplicates([]) == []
