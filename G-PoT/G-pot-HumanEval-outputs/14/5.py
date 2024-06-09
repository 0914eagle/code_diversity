
from typing import List

def skjkasdkd(lst: List[int]) -> int:
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_digits_sum = 0
    largest_prime = 0

    for num in lst:
        if is_prime(num):
            if num > largest_prime:
                largest_prime = num

    if largest_prime == 0:
        return 0

    for digit in str(largest_prime):
        prime_digits_sum += int(digit)

    return prime_digits_sum
