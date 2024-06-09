
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
            if b[i] + 1 == b[j] or b[i] - 1 == b[j]:
                min_changes = 1
                break
        if min_changes == 1:
            break
    if min_changes == 1:
        return min_changes
    for i in range(n):
        for j in range(i+1, n):
            if b[i] + 1 == b[j] and b[j] + 1 == b[i+2]:
                min_changes = 2
                break
        if min_changes == 2:
            break
    if min_changes == 2:
        return min_changes
    for i in range(n):
        for j in range(i+1, n):
            if b[i] - 1 == b[j] and b[j] - 1 == b[i+2]:
                min_changes = 2
                break
        if min_changes == 2:
            break
    if min_changes == 2:
        return min_changes
    for i in range(n):
        for j in range(i+1, n):
            if b[i] + 1 == b[j] and b[j] + 1 == b[i+2] and b[i+2] + 1 == b[i+3]:
                min_changes = 3
                break
        if min_changes == 3:
            break
    if min_changes == 3:
        return min_changes
    for i in range(n):
        for j in range(i+1, n):
            if b[i] - 1 == b[j] and b[j] - 1 == b[i+2] and b[i+2] - 1 == b[i+3]:
                min_changes = 3
                break
        if min_changes == 3:
            break
    if min_changes == 3:
        return min_changes
    return -1

