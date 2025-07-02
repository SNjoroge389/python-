def find_max(lst):
    """
    Returns the largest number in the list.
    Returns None if the list is empty.
    """
    if len(lst) == 0:
        return None

    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value
