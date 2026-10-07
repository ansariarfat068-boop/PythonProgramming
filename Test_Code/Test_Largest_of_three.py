from Code.Largest_of_three import largest_of_three

def test_first():
    result = largest_of_three(10, 20, 25)
    assert result == 25


def test_second():
    result = largest_of_three(1, 9, 6)
    assert result == 9


def test_third():
    result = largest_of_three(8, 6, 3)
    assert result == 8