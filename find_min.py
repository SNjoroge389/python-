def find_min(lst):
    """
    Returns the smallest number in the list.
    Returns None if the list is empty.
    """
    if len(lst) == 0:
        return None

    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value
