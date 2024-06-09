
def get_compatible_pairs(n, l, r):
    compatible_pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if l[i] == r[j] or l[i] == "?" or r[j] == "?":
                compatible_pairs.append([i, j])
    return compatible_pairs

