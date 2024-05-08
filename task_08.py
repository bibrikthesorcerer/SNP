# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com
import re
from math import prod
def get_num_from_str(string:str):
    try:
        digits = re.findall(r"[0-9]", string)
        digits = [int(num) for num in digits]
        return prod(digits)
    except TypeError:
        return None

def multiply_numbers(input):
    if isinstance(input, str):
        return get_num_from_str(input)
    elif iter(input):
        pass
    else:
        try:
            return get_num_from_str(str(input))
        except TypeError:
            return None
        
#print(multiply_numbers(2.3))

print(iter(2.3))