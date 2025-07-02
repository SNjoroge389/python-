def sum_of_elements(lst):
    """
    Returns the sum of all elements in the list.
    Avoids using the built-in sum() function.
    """
    total = 0
    for num in lst:
        total += num
    return total
