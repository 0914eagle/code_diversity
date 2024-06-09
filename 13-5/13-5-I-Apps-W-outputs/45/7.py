
import math

def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def count_factorizations(x, y):
    factors = factorize(x)
    num_factorizations = 1
    for i in range(y):
        num_factorizations *= math.factorial(len(factors))
        factors.pop()
    return num_factorizations % (10**9 + 7)

def main():
    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        print(count_factorizations(x, y))

if __name__ == '__main__':
    main()

