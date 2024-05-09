# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

def merge_dict_priority(dict1: dict, dict2: dict) -> dict:
    """
    Merge two dicts in one dict sorted by values with priority, excluding values < 10.
    """
    # объединяем два словаря, забираем items
    prioritized = (dict1 | dict2).items()
    # фильтруем значения < 10 
    filtered =  [[k, v] for k,v in prioritized if v >= 10]
    # сортируем по значениям
    items_sort = sorted(filtered, key=(lambda x: x[1]))
    # собираем обратно в словарь и возвращаем
    return dict(items_sort)

def connect_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Merge two dictionaries based on the sum of their values.
    If the sum of values in the first dictionary is greater, it has priority;
    otherwise, the second dictionary has priority.
    """
    # посчитаем сумму значений для каждого словаря
    s_val_1 = sum(list(dict1.values()))
    s_val_2 = sum(list(dict2.values()))

    # если первая сумма больше - то у первого словаря приоритет, иначе аналогично
    return merge_dict_priority(dict2, dict1)\
           if s_val_1 > s_val_2 \
           else merge_dict_priority(dict1, dict2)