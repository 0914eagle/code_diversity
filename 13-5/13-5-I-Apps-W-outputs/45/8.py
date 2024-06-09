
import math

def is_y_factorization(x, y, factors):
    if len(factors) != y:
        return False
    prod = 1
    for f in factors:
        prod *= f
    return prod == x

def count_y_factorizations(x, y):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            j = x // i
            if is_y_factorization(x, y, [i, j]):
                count += 1
    return count

def solve(x, y):
    return count_y_factorizations(x, y) % (10**9 + 7)

if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        x, y = map(int, input().split())
        print(solve(x, y))

