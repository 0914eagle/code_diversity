
import math

def largest_divisor(n: int) -> int:
    def is_divisor(x, n):
        return n % x == 0

    def find_largest_divisor(n):
        for i in range(n - 1, 0, -1):
            if is_divisor(i, n):
                return i

    return find_largest_divisor(n)

if __name__ == "__main__":
    n = int(input())
    print(largest_divisor(n))
