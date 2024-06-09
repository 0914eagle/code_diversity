
def count_pairs(a, b, c):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == b[i] == c[i] and a[j] == b[j] == c[j]:
                count += 1
    return count

