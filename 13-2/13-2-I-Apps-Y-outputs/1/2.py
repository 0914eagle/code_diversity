
def f1(n, k, d):
    # find all possible pairs of boxes that can be given as gifts
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if (d[i] + d[j]) % k == 0:
                pairs.append((i, j))
    
    # find the maximum number of pairs that can be given as gifts
    max_pairs = 0
    for i in range(len(pairs)):
        pair = pairs[i]
        if pair not in pairs[i+1:]:
            max_pairs += 1
    
    return max_pairs

def f2(...):
    ...

if __name__ == '__main__':
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    print(f1(n, k, d))

