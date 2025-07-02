def has_duplicates(lst):
    """
    Returns True if there are duplicate values in the list.
    Uses nested loops to compare each pair of elements.
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False
