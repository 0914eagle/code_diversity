
def f1(n, k, d):
    # find all pairs of boxes that can be combined to form a gift
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if (d[i] + d[j]) % k == 0:
                pairs.append((i, j))
    
    # find the maximum number of pairs that can be formed
    max_pairs = 0
    for i in range(1, len(pairs)+1):
        pairs_combinations = itertools.combinations(pairs, i)
        for combination in pairs_combinations:
            if len(set(combination)) == i:
                max_pairs = max(max_pairs, i)
    
    return max_pairs

def f2(n, k, d):
    # find all pairs of boxes that can be combined to form a gift
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if (d[i] + d[j]) % k == 0:
                pairs.append((i, j))
    
    # find the maximum number of pairs that can be formed
    max_pairs = 0
    for i in range(1, len(pairs)+1):
        pairs_combinations = itertools.combinations(pairs, i)
        for combination in pairs_combinations:
            if len(set(combination)) == i:
                max_pairs = max(max_pairs, i)
    
    return max_pairs

if __name__ == '__main__':
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    print(f1(n, k, d))
    print(f2(n, k, d))

