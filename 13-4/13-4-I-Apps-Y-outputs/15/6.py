
def solve(b):
    n = len(b)
    if n == 1:
        return 0
    if n == 2:
        if b[0] == b[1]:
            return 0
        else:
            return -1
    # find the common difference of the sequence
    common_diff = b[1] - b[0]
    for i in range(2, n):
        if b[i] - b[i-1] != common_diff:
            return -1
    # check if the sequence can be changed to an arithmetic progression
    min_changes = -1
    for i in range(n):
        if b[i] != common_diff * (i - 1):
            min_changes = i
            break
    return min_changes

