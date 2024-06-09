
def solve(n, arr):
    arr.sort()
    count = 0
    for i in range(n):
        if arr[i] != 0:
            count += n - i
    return count

