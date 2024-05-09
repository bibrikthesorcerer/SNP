# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

def sort_list(lst: list[int]) -> list[int]:
    """
    Swap all minimum and maximum values in a list and append one minimum to the end
    """
    # с пустыми массивами не работаем
    if not lst:
        return lst

    # списки индексов - после прохода цикла по списку lst здесь будут лежать
    # индексы минимальных и максимальных значений в списке
    max_ind = [0,]
    min_ind = [0,]
    
    # по умолчанию считаем максимальным элементом первый
    max_num = lst[0]
    min_num = lst[0]

    for i in range(len(lst)):
        # если нашли новый минимум, то очистим старые индексы, внесём новый и обновим минимум
        if lst[i] < min_num:
            min_ind.clear()
            min_ind.append(i)
            min_num = lst[i]

        # если нашли новый максимум, то поступаем как с минимумом
        if lst[i] > max_num:
            max_ind.clear()
            max_ind.append(i)
            max_num = lst[i]
        
        # если нашли новый индекс максимума или минимума, добавляем
        if lst[i] == min_num:
            min_ind.append(i)
        if lst[i] == max_num:
            max_ind.append(i)
    
    # меняем максимумы и минимумы
    for i in max_ind:
        lst[i] = min_num
    for i in min_ind:
        lst[i] = max_num
    
    # добавляем минимум в конец списка
    lst.append(min_num)
    return lst