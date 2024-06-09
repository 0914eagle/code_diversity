
def swap_elements(arr):
    n = len(arr)
    count = 0
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
                pairs.append((i, j))
    return count, pairs

