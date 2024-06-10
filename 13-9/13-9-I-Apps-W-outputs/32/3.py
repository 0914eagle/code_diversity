
import math

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def choose(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def solve(n, a, b):
    count = 0
    for i in range(1, n+1):
        if i != a and i != b:
            count += choose(n-1, i-1)
    return count % (10**9 + 7)

def main():
    n, a, b = map(int, input().split())
    print(solve(n, a, b))

if __name__ == '__main__':
    main()

