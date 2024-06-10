
import math

def largest_divisor(n: int) -> int:
    def is_divisor(n, divisor):
        return n % divisor == 0

    def find_largest_divisor(n):
        for i in range(n - 1, 0, -1):
            if is_divisor(n, i):
                return i

    return find_largest_divisor(n)

if __name__ == "__main__":
    n = int(input())
    print(largest_divisor(n))
