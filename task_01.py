# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

import re
import string as s

def format_palindrome(string: str) -> str:
    """
    Formats a given object into a palindrome by removing all punctuation and whitespace, 
    and converting all uppercase letters to lowercase. 
    """
    # get rid of all punctuation + whitespace
    f_string = re.subn(fr"[{s.punctuation}{s.whitespace}]", "",string)[0]

    # replace uppercase with lowercase letters
    return f_string.casefold()

def is_palindrome(string) -> bool:
    """
    A function that checks if a given object is a palindrome.
    Given object should have a __str__() method.
    """
    # format the string
    s_format = format_palindrome(string.__str__())
    # check if string is palindrome
    return s_format == s_format[::-1]