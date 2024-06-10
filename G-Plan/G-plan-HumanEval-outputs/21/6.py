
from typing import Tuple

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    char_set = set(c)
    result = ''.join(char for char in s if char not in char_set)
    is_palindrome_result = is_palindrome(result)
    return result, is_palindrome_result

s, c = input().strip().split()
result, is_palindrome_result = reverse_delete(s, c)
print(result, is_palindrome_result)
