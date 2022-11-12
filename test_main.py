from main import is_squares_of_list


def test_empty_lists():
    assert is_squares_of_list([], []) is True


def test_one_element():
    assert is_squares_of_list([1], [1]) is True


def test_multiple_elements_unordered():
    assert is_squares_of_list([1, 2, 1, 3, 2, 1, 2], [9, 1, 4, 9, 1]) is True


def test_wrong_same_list():
    assert is_squares_of_list([1, 2, 3], [1, 2, 3]) is False


def test_list_empty_squares_not():
    assert is_squares_of_list([], [1, 4, 9]) is False


def test_squares_empty_list_not():
    assert is_squares_of_list([1, 2, 3], []) is False


def test_negative_numbers_in_list():
    assert is_squares_of_list([-1, -2, -3], [1, 4, 9]) is True


def test_negative_numbers_in_squares():
    assert is_squares_of_list([-1, -2, -3], [-1, -4, -9]) is False


def test_1_000_000_elements_list():
    _list = [i for i in range(1_000_000)]
    squares = [i * i for i in _list]
    assert is_squares_of_list(_list, squares) is True
