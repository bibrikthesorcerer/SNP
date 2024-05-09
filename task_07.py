# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

def combine_anagrams(words: list[str]) -> list[list[str]]:
    """
    Cluster words based on sets of letters they're made of.
    """
    anagr_dict = {}

    for word in words:
        # сортируем слово в алфавитном порядке
        w_sorted = "".join(sorted(word))
        # достаем значение по отсортированной строке и либо инициализируем либо приписываем новое слово
        anagr_dict[w_sorted] = anagr_dict.get(w_sorted, []) + [word]
    # из всего словаря нам нужны лишь значения
    return list(anagr_dict.values())