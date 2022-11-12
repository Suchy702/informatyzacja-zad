from main import are_squares_of_list_in_another_list


def test_empty_lists():
    assert are_squares_of_list_in_another_list([], []) is True


def test_empty_list_squares_not():
    assert are_squares_of_list_in_another_list([], [1, 2]) is True


def test_one_element():
    assert are_squares_of_list_in_another_list([1], [1]) is True


def test_diff_numbers_in_squares():
    assert are_squares_of_list_in_another_list([1, 2], [1, 2, 3, 4]) is True


def test_missing_square():
    assert are_squares_of_list_in_another_list([1, 2, 3], [9, 1, 5, 5]) is False


def test_unordered_and_duplicates():
    assert are_squares_of_list_in_another_list([3, 5, 2], [25, 4, 4, 4, 9, 9]) is True


def test_negative_numbers():
    assert are_squares_of_list_in_another_list([-2, -5, -1], [25, 1, 4]) is True


def test_negative_squares():
    assert are_squares_of_list_in_another_list([-1, -2, -5], [-1, -4, -25]) is False


def test_1_000_000_elements_and_in_square_some_othera_numbers():
    _list = [i for i in range(1_000_000)]
    squares = [i * i for i in range(1_000_000)] + [i for i in range(5, 1000, 6)]
    assert are_squares_of_list_in_another_list(_list, squares) is True
