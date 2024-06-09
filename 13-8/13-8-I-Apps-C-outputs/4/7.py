
def solve(n, arr):
    count = 0
    for i in range(n-1):
        if arr[i] == 0 and arr[i+1] == 0:
            count += 1
        elif arr[i] == 2 and arr[i+1] == 2:
            count += 1
    if arr[n-1] == 0 or arr[n-1] == 2:
        count += 1
    return count

