
def solve(m, k, a, b):
    # Calculate the target fractions
    f = [ai / sum(a) for ai in a]
    
    # Calculate the current fraction of each type of sweet
    s = [b.count(i) for i in range(1, m + 1)]
    
    # Calculate the maximum number of additional sweets that can be bought
    max_sweets = 0
    for i in range(m):
        if s[i] > f[i]:
            max_sweets += 1
        elif s[i] < f[i]:
            max_sweets += 2
    
    return max_sweets

