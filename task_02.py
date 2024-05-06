# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

def coincidence(lst=[], rng=None):
    """
    Return a list of elements from lst whose values fit in rng.
    
    Parameters:
        lst (list) = []: A list of elements.
        rng (range) = None: A range object representing a range of numbers.
    
    Returns:
        list: A list of elements that fall within the specified range.
    """
    res_lst = []
    for elem in lst:
        # let's check if element is even a number first of all
        if isinstance(elem, int) or isinstance(elem, float):
            # now let's check if it fits in the range
            if rng.start <= elem and elem < rng.stop:
                # if elem fits in the range, append this bad boy
                res_lst.append(elem)
    # return the list
    return res_lst