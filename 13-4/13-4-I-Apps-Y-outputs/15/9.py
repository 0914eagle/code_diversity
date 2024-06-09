
def solve(b):
    n = len(b)
    if n == 1:
        return 0
    if n == 2:
        if b[0] == b[1]:
            return 0
        else:
            return -1
    # sort the list in ascending order
    b.sort()
    # initialize the minimum number of elements to change
    min_elements = 0
    # loop through the list and check if the difference between each two elements is the same
    for i in range(n-1):
        if b[i+1] - b[i] != b[1] - b[0]:
            min_elements += 1
    # if the minimum number of elements to change is greater than the length of the list, it is impossible to make an arithmetic progression
    if min_elements > n:
        return -1
    else:
        return min_elements

