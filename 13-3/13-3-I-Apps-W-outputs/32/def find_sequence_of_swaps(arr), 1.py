
def find_sequence_of_swaps(arr):
    n = len(arr)
    swaps = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                swaps.append([i, j])
    return swaps

