
from Code.Word_Frequency  import word_frequency


def test_word_frequency():
    assert word_frequency("hello world hello") == {
        "hello": 2,
        "world": 1
    }


def test_empty_sentence():
    assert word_frequency("") == {}


def test_same_word():
    assert word_frequency("python python python") == {
        "python": 3
    }
