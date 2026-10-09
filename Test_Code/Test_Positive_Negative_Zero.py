from Code.Positive_Negative_Zero import positive_negative_zero

def test_positive():
    assert positive_negative_zero(10) == "POSITIVE"

def test_negative():
    assert positive_negative_zero(-5) == "NEGATIVE"

def test_zero():
    assert positive_negative_zero(0) == "ZERO"


