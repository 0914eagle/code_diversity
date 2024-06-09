
def solve(p, foe_pairs):
    n = len(p)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if not any(p[i] in pair and p[j] in pair for pair in foe_pairs):
                count += 1
    return count

