
from typing import Tuple

def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    even_count = 0
    odd_count = 0

    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    print((even_count, odd_count))

even_odd_palindrome(int(input()))
