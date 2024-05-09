# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

import re
from math import prod

def get_num_from_str(string: str) -> list[int]:
    """
    Extract all digits from string.
    """
    digits = re.findall(r"[0-9]", string) # находим цифры
    digits = [int(num) for num in digits] # приводим к int
    return digits

def multiply_numbers(input=None):
    """
    Get a product of all numbers in input.
    """
    # преобразуем input в строку и вытаскиваем все цифры
    nums = get_num_from_str(input.__str__())
    # возвращаем произведение цифр, если они есть
    return prod(nums) if nums else None