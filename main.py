def are_squares_of_list_in_another_list(_list: list[int], squares: list[int]) -> bool:
    return {i*i for i in _list}.issubset(set(squares))


