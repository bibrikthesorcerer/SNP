# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

def max_odd(arr: list):
    """
    Find the maximum odd number in a given array.
    """
    max_odd_num = None
    for elem in arr:
        # если элемент не int - попробуем его привести к int. 
        if not isinstance(elem, int):
                if isinstance(elem, float) and elem.is_integer():
                    elem = int(elem)
                else:
                     continue
        # если элемент - нечетное число, то сравним его с максимумом 
        # или инициализируем максимум, если он пуст
        if elem % 2 != 0:
            if max_odd_num is None or elem > max_odd_num:
                max_odd_num = elem
    return max_odd_num