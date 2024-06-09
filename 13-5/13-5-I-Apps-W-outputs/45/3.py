
import sys

def factorize(x, y):
    factors = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            factors.append(i)
            if x // i != i:
                factors.append(x // i)
    return factors

def count_factorizations(x, y):
    factors = factorize(x, y)
    num_factorizations = 1
    for i in range(len(factors)):
        num_factorizations *= len(factors) - i
    return num_factorizations % (10 ** 9 + 7)

def main():
    q = int(input())
    for i in range(q):
        x, y = map(int, input().split())
        print(count_factorizations(x, y))

if __name__ == '__main__':
    main()

