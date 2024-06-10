
import math

def largest_divisor(n: int) -> int:
    def iterative_largest_divisor(n: int) -> int:
        for i in range(n - 1, 0, -1):
            if n % i == 0:
                return i

    def optimized_largest_divisor(n: int) -> int:
        for i in range(int(math.sqrt(n)), 0, -1):
            if n % i == 0:
                return max(i, n // i)

    return optimized_largest_divisor(n)

if __name__ == "__main__":
    n = int(input())
    print(largest_divisor(n))
