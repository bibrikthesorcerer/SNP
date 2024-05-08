# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

def combine_anagrams(words: list):
    anagr_dict = dict()

    for word in words:
        # сортируем слово в алфавитном порядке
        w_sorted = "".join(sorted(word))
        # посмотрим что лежит в словаре по этому сортированному слову
        anagr_lst = anagr_dict.get(w_sorted)
        # если ничего, то инициализируем список по ключу
        if anagr_lst is None:
            anagr_dict.update({w_sorted: [word]})
        # иначе добавим в список новое слово
        else:
            anagr_lst.append(word)
    return list(anagr_dict.values())

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))