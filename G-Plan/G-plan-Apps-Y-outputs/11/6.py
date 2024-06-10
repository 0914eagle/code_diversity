
from itertools import combinations

def max_prettiness(n, problems):
    max_total = 0
    for i in range(1, 4):
        for comb in combinations(problems, i):
            if all(a % b != 0 and b % a != 0 for a, b in combinations(comb, 2)):
                max_total = max(max_total, sum(comb))
    return max_total

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        problems = list(map(int, input().split()))
        result = max_prettiness(n, problems)
        print(result)
