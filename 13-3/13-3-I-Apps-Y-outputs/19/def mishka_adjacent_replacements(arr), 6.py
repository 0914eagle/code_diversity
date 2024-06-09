
def mishka_adjacent_replacements(arr):
    n = len(arr)
    for i in range(1, 5*10**8+1):
        for j in range(i-1, n, i):
            if arr[j] == i-1:
                arr[j] = i
            if arr[j] == i:
                arr[j] = i-1
    return arr

