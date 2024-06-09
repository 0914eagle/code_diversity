
def solve(arr):
    count = 0
    while arr:
        count += 1
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                arr = arr[:i] + arr[i+2:]
                break
    return count

