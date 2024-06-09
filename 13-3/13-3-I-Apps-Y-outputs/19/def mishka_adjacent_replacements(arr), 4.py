
def mishka_adjacent_replacements(arr):
    n = len(arr)
    for i in range(1, 500000001):
        for j in range(i, n, i):
            if arr[j] == i:
                arr[j] = i + 1
            if arr[j] == i + 1:
                arr[j] = i
    return arr

