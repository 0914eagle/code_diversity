
from typing import Tuple

def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def count_palindromes(start, end):
        count = 0
        for num in range(start, end + 1):
            if is_palindrome(num):
                count += 1
        return count

    even_count = count_palindromes(1, n)
    odd_count = count_palindromes(1, n)

    print((even_count, odd_count))

even_odd_palindrome(int(input()))
