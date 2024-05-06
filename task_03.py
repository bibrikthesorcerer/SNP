# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

def max_odd(arr):
    """
    Find the maximum odd number in a given array.

    Parameters:
        arr (list): A list of integers or objects that can be converted to integers.

    Returns:
        int or None: The maximum odd number in the array, or None if no odd number is found.
    """
    res = -1
    for elem in arr:
        if not isinstance(elem, int):
            try:
                elem = int(elem)
            except (ValueError, TypeError):
                continue
        if elem % 2 != 0 and elem > res:
            res = elem
    return None if res == -1 else res