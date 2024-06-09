
def solve(b):
    n = len(b)
    if n == 1:
        return 0
    if n == 2:
        if b[0] == b[1]:
            return 0
        else:
            return -1
    # find the common difference of the AP
    common_diff = b[1] - b[0]
    for i in range(2, n):
        if b[i] - b[i-1] != common_diff:
            return -1
    # find the minimum number of elements to change
    min_elements = 0
    for i in range(n):
        if b[i] % common_diff != 0:
            min_elements += 1
    return min_elements

