def is_squares_of_list(_list: list[int], squares: list[int]) -> bool:
    return {i*i for i in _list} == set(squares)

