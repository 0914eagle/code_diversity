
from itertools import combinations

def max_prettiness(n, prettiness_values):
    max_total_prettiness = 0
    for i in range(1, min(n, 3) + 1):
        for comb in combinations(prettiness_values, i):
            if all(comb[j] % comb[k] != 0 for j in range(i) for k in range(j)):
                max_total_prettiness = max(max_total_prettiness, sum(comb))
    return max_total_prettiness

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        prettiness_values = list(map(int, input().split()))
        result = max_prettiness(n, prettiness_values)
        print(result)
