# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

import re
import string as s

def rm_punct_and_lower(string: str) -> str:
    """
    Remove punctuation in string and lower all letters
    """
    # всю пунктуацию выкидываем, из кортежа берем только строку
    f_string = (re.subn(fr"[{s.punctuation}]", "",string))[0]
    # заглавные буквы меняем на прописные
    return f_string.casefold()

def count_words(string: str) -> dict:
    """
    Count frequency of use of words in string.
    """
    freq_of_use = {}
    
    # отформатируем строку
    f_string = rm_punct_and_lower(string)
    # разделяем строку на токены. разделители - 1+ символ пробелов\табуляции и т.д.
    words = re.split(fr"[{s.whitespace}]+", f_string)
    
    for w in words:
        # если слово в словаре уже есть, увеличим количество вхождений, иначе инициализируем единицей
        freq_of_use[w] = freq_of_use.get(w, 0) + 1
    return freq_of_use