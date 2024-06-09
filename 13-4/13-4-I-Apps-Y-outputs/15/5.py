
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
    if len(set(diff)) != 1:
        return -1
    count = 0
    for i in range(n):
        if b[i] != b[0] + i * diff[0]:
            count += 1
    return count

