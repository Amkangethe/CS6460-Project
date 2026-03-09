from tasks.running_sum import running_sum

def test_basic():
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]

def test_single_element():
    assert running_sum([5]) == [5]

def test_empty_list():
    assert running_sum([]) == []

def test_negative_numbers():
    assert running_sum([-1, -2, -3]) == [-1, -3, -6]