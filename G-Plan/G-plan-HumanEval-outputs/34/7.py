
import math

def largest_divisor(n: int) -> int:
    def is_divisor(x, n):
        return n % x == 0

    def find_largest_divisor(n):
        for i in range(int(math.sqrt(n)), 0, -1):
            if is_divisor(i, n):
                return i
        return 1

    n = int(input())
    result = find_largest_divisor(n)
    print(result)

if __name__ == "__main__":
    largest_divisor(int(input()))
