
from Code.Fibonacci_Series import fibonacci

def test_fibonacci_5():
    assert fibonacci(5) == [0, 1, 1, 2, 3]

def test_fibonacci_7():
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_1():
    assert fibonacci(1) == [0]

def test_fibonacci_0():
    assert fibonacci(0) == []

def test_fibonacci_2():
    assert fibonacci(2) == [0, 1]

def test_fibonacci_3():
    assert fibonacci(3) == [0, 1, 1]

def test_fibonacci_4():
    assert fibonacci(4) == [0, 1, 1, 2]

def test_fibonacci_6():
    assert fibonacci(6) == [0, 1, 1, 2, 3, 5]
