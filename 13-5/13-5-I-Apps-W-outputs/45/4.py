
import math

def is_y_factorization(x, y, factors):
    if len(factors) != y:
        return False
    product = 1
    for factor in factors:
        product *= factor
    return product == x

def count_y_factorizations(x, y):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    count = 0
    for i in range(len(factors)):
        for j in range(i + 1, len(factors)):
            if is_y_factorization(x, y, [factors[i], factors[j]]):
                count += 1
    return count

def solve(x, y):
    return count_y_factorizations(x, y) % (10**9 + 7)

if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        x, y = map(int, input().split())
        print(solve(x, y))

