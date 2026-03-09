from tasks.reverse_words import reverse_words

def test_basic():
    assert reverse_words("hello world") == "world hello"

def test_single_word():
    assert reverse_words("python") == "python"

def test_empty_string():
    assert reverse_words("") == ""

def test_multiple_spaces():
    assert reverse_words("hello   world") == "world hello"