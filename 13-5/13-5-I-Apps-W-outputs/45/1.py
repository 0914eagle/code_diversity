
import sys

def get_y_factorizations(x, y):
    factorizations = []
    for i in range(1, x + 1):
        if x % i == 0 and i <= y:
            factorizations.append(i)
    return factorizations

def count_distinct_factorizations(x, y):
    factorizations = get_y_factorizations(x, y)
    distinct_factorizations = set()
    for factorization in factorizations:
        distinct_factorizations.add(tuple(factorization))
    return len(distinct_factorizations)

def main():
    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        print(count_distinct_factorizations(x, y))

if __name__ == '__main__':
    main()

