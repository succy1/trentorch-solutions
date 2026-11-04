def count_comparisons_linear_search(arr, target):
    """
    arr:    a list of numbers
    target: the value being searched for

    Returns:
        (found, comparisons): found is True if target is in arr, False
        otherwise. comparisons is the number of element-to-target
        comparisons actually performed (stop as soon as a match is
        found -- don't keep scanning).
    """
    # TODO: Implement a left-to-right linear scan, counting comparisons.
    count = 0
    for v in arr:
        count += 1
        if v == target:
            return (True, count)
    return (False, count)

def count_comparisons_binary_search(sorted_arr, target):
    """
    sorted_arr: a list of numbers, already sorted ascending
    target:     the value being searched for

    Returns:
        (found, comparisons): same shape as count_comparisons_linear_search,
        but using binary search -- each comparison must actually halve
        the remaining search space.
    """
    # TODO: Implement binary search from Theory, counting one
    # comparison per midpoint check.
    start, end = 0, len(sorted_arr) - 1
    count = 0

    while start <= end:
        middle = (start + end) // 2
        count += 1
        if sorted_arr[middle] == target:
            return (True, count)
        elif sorted_arr[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    return (False, count)
