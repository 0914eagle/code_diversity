
from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    
    # delete all characters in s that are equal to any character in c
    result = ''.join([char for char in s if char not in c])
    
    # check if the result string is palindrome
    is_palindrome = result == result[::-1]
    
    return result, is_palindrome

