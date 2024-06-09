
import math

def factorize(x, y):
    factors = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            factors.append(i)
            if x // i != i:
                factors.append(x // i)
    factors.sort()
    return factors[:y]

def count_factorizations(x, y):
    factors = factorize(x, y)
    num_factorizations = 1
    for i in range(y):
        num_factorizations *= len(factors) - i
    return num_factorizations % (10**9 + 7)

def main():
    q = int(input())
    for i in range(q):
        x, y = map(int, input().split())
        print(count_factorizations(x, y))

if __name__ == '__main__':
    main()

