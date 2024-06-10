
import math

def largest_divisor(n: int) -> int:
    def iterative_largest_divisor(n: int) -> int:
        for i in range(n - 1, 0, -1):
            if n % i == 0:
                return i
        return 1

    def optimized_largest_divisor(n: int) -> int:
        for i in range(int(math.sqrt(n)), 0, -1):
            if n % i == 0:
                return max(i, n // i)
        return 1

    if n <= 0:
        return 1

    return optimized_largest_divisor(n)

if __name__ == "__main__":
    n = int(input().strip())
    print(largest_divisor(n))
