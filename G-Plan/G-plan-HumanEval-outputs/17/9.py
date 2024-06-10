
from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def delete_chars(s: str, chars: set) -> str:
        return ''.join(char for char in s if char not in chars)

    chars_set = set(c)
    result = delete_chars(s, chars_set)
    is_palindrome_result = is_palindrome(result)

    return result, is_palindrome_result

if __name__ == "__main__":
    s, c = input().strip().split()
    result, is_palindrome_result = reverse_delete(s, c)
    print(result, is_palindrome_result)
