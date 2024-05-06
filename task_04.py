# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

def sort_list(lst):
    """
    Swaps all minimum and maximum values in a list and appends one minimum to the end
    
    Parameters:
        lst (list): A list of numbers to be swapped
    
    Returns:
        list: List with swapped values and additional minimum appended
    """
    # init lists of indexes for swapping
    max_ind = [0,]
    min_ind = [0,]
    # init min and max values
    max = lst[0]
    min = lst[0]

    for elem in lst:
        # if found new min
        if elem < min:
            # clear old min indexes
            min_ind.clear()
            # add new min index
            min_ind.append(i)
            # update min
            min = elem

        # if found new max
        if elem > max:
            # clear old max indexes
            max_ind.clear()
            # add new max index
            max_ind.append(i)
            # update max
            max = elem
        
        # if found equal, add new index to the list
        if elem == min:
            min_ind.append(i)
        if elem == max:
            max_ind.append(i)
    
    # swap values
    for i in max_ind:
        lst[i] = min
    for i in min_ind:
        lst[i] = max
    
    # append minimum to the end
    lst.append(min)
    return lst