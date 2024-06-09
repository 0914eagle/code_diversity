
def solve(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
    return swaps

