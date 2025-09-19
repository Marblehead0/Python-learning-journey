from intermediate.week3.util_string import reverse_words

def test_basic():
    assert reverse_words("hello world") == "world hello"

def test_single_word():
    assert reverse_words("Python") == "Python"

def test_extra_spaces():
    assert reverse_words("  a  b   c ") == "c b a"
