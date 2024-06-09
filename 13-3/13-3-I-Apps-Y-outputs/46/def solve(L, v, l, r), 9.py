
def solve(L, v, l, r):
    count = 0
    for i in range(1, L+1):
        if i % v == 0 and i not in range(l, r+1):
            count += 1
    return count

