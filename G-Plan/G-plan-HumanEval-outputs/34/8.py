
import math

def largest_divisor(n: int) -> int:
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i
    return 1

if __name__ == "__main__":
    n = int(input())
    print(largest_divisor(n))
