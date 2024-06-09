
def min_operations(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            count += 1
    return count

