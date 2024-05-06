# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

import re
import string as s

def format_palindrome(string):
    """
    Formats a given object into a palindrome by removing all punctuation and whitespace, 
    and converting all uppercase letters to lowercase. 

    Args:
        string (str): The object to be formatted.

    Returns:
        str: The formatted palindrome string.
    """
    # get rid of all punctuation + whitespace
    f_tuple = re.subn(fr"[{s.punctuation}{s.whitespace}]", "",string)

    # subn returned a tuple with formatted string as element at 0
    f_string = f_tuple[0]

    # replace uppercase with lowercase letters
    formatted = f_string.lower()
    return formatted

def is_palindrome(string):
    """
    A function that checks if a given string is a palindrome.

    Parameters:
        string (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    if isinstance(string, str):
        # forma the string
        s_format = format_palindrome(s)
        # get the formatted string length
        s_len = len(s_format)
        # check if string is palindrome
        for i in range(0, int(s_len/2)):
            print(f"{s_format[i]} ? {s_format[s_len - i - 1]}")
            if (s_format[i] != s_format[s_len - i - 1]):
                return False
            
        return True
    else:
        return False