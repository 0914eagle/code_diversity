
from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    def is_palindrome(string: str) -> bool:
        return string == string[::-1]

    def delete_chars(s: str, chars_to_delete: set) -> str:
        return ''.join(char for char in s if char not in chars_to_delete)

    chars_to_delete = set(c)
    modified_string = delete_chars(s, chars_to_delete)
    is_palindrome_result = is_palindrome(modified_string)

    return modified_string, is_palindrome_result

if __name__ == "__main__":
    s, c = input().strip().split()
    result, is_palindrome_result = reverse_delete(s, c)
    print(result, is_palindrome_result)
