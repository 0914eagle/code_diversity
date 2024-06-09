
def mishka_adjacent_replacements(arr):
    n = len(arr)
    for i in range(1, 5*10**8+1):
        for j in range(i-1, n, 2*i-1):
            if j+i-1 < n and arr[j] == i-1 and arr[j+i-1] == i:
                arr[j] = i+1
                arr[j+i-1] = i-1
    return arr

