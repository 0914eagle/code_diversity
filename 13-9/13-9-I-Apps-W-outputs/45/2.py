
import math
import sys

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return divisors

def get_expected_value(n, k):
    divisors = get_divisors(n)
    total = 0
    for d in divisors:
        total += d
    return total / len(divisors) ** k

def main():
    n, k = map(int, input().split())
    print(get_expected_value(n, k))

if __name__ == '__main__':
    main()

