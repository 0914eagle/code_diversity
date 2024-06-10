
from itertools import combinations

def max_prettiness(n, problems):
    max_total = 0
    for i in range(1, 4):
        for comb in combinations(problems, i):
            if all(comb[j] % comb[k] != 0 for j in range(len(comb)) for k in range(j+1, len(comb))):
                max_total = max(max_total, sum(comb))
    return max_total

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        problems = list(map(int, input().split()))
        result = max_prettiness(n, problems)
        print(result)
