
from Code.Remove_Duplicate import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_no_duplicates():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

def test_empty_list():
    assert remove_duplicates([]) == []
