
def solve(b):
    n = len(b)
    if n == 1:
        return 0
    if n == 2:
        if b[0] == b[1]:
            return 0
        else:
            return -1
    diff = [b[i+1] - b[i] for i in range(n-1)]
    if len(set(diff)) == 1:
        return 0
    min_changes = -1
    for i in range(n):
        for j in range(i+1, n):
            if b[i] == b[j]:
                continue
            changes = 0
            for k in range(n):
                if k == i or k == j:
                    continue
                if b[k] < min(b[i], b[j]):
                    changes += 1
                elif b[k] > max(b[i], b[j]):
                    changes += 1
            if changes < min_changes or min_changes == -1:
                min_changes = changes
    return min_changes

