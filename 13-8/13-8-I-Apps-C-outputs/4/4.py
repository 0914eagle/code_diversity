
def solve(n, arr):
    count = 0
    for i in range(n):
        if arr[i] == 0 or arr[i] == 1:
            count += 1
    return count

