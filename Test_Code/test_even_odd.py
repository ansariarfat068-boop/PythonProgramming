from Code.even_odd import check_even_odd

def test_even_10():
    assert check_even_odd(10)=="even"

def test_even_20():
    assert check_even_odd(20)=="even"

def test_odd_11():
    assert check_even_odd(11)=="odd"

def test_odd_25():
    assert check_even_odd(25)=="odd"  


print("ALL TEST PASSED") 