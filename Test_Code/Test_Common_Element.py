from Code.Common_Element import common_element

def test_common_element():
    assert common_element([1, 2, 3], [2, 3, 4]) == [2, 3]

def test_no_common_element():
    assert common_element([1, 2], [3, 4]) == []