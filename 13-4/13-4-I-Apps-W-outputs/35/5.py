
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def count_swaps(arr):
    swaps = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                swaps += 1
    return swaps

def get_min_swaps(arr):
    min_swaps = count_swaps(arr)
    min_pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps = count_swaps(arr)
                if swaps < min_swaps:
                    min_swaps = swaps
                    min_pairs = [(i, j)]
                elif swaps == min_swaps:
                    min_pairs.append((i, j))
                arr[i], arr[j] = arr[j], arr[i]
    return min_swaps, min_pairs

arr = [4, 0, 3, 1, 2]
print(get_min_swaps(arr))

