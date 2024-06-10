
from itertools import combinations

def max_prettiness(n, prettiness):
    max_total = 0
    for i in range(1, 4):
        for comb in combinations(prettiness, i):
            valid_comb = True
            for pair in combinations(comb, 2):
                if pair[0] % pair[1] == 0 or pair[1] % pair[0] == 0:
                    valid_comb = False
                    break
            if valid_comb:
                max_total = max(max_total, sum(comb))
    return max_total

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        prettiness = list(map(int, input().split()))
        result = max_prettiness(n, prettiness)
        print(result)
