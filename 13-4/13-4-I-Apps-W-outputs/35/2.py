
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def get_min_swaps(arr):
    n = len(arr)
    count = 0
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
                pairs.append((i, j))
    return count, pairs

arr = [4, 0, 3, 1, 2]
insertion_sort(arr)
count, pairs = get_min_swaps(arr)
print(count, pairs)

