
from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def filter_characters(s: str, c_set: set) -> str:
        return ''.join(char for char in s if char not in c_set)

    c_set = set(c)
    filtered_string = filter_characters(s, c_set)
    is_palindrome_result = is_palindrome(filtered_string)

    return filtered_string, is_palindrome_result

s, c = input().strip().split()
result, is_palindrome_result = reverse_delete(s, c)
print(result, is_palindrome_result)
