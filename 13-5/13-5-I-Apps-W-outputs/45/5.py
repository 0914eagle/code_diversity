
import math

def get_y_factorizations(x, y):
    factorizations = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            j = x // i
            if i <= y and j <= y:
                factorizations.append([i, j])
            if i != j and i <= y and j <= y:
                factorizations.append([j, i])
    return factorizations

def count_distinct_factorizations(x, y):
    factorizations = get_y_factorizations(x, y)
    distinct_factorizations = set()
    for factorization in factorizations:
        distinct_factorizations.add(tuple(factorization))
    return len(distinct_factorizations)

def main():
    q = int(input())
    for i in range(q):
        x, y = map(int, input().split())
        print(count_distinct_factorizations(x, y) % (10**9 + 7))

if __name__ == '__main__':
    main()

