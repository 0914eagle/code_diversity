
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def find_min_swaps(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

def find_min_swaps_pairs(arr):
    n = len(arr)
    count = 0
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
                pairs.append((i, j))
    return count, pairs

n = int(input())
arr = list(map(int, input().split()))
insertion_sort(arr)
count = find_min_swaps(arr)
pairs = find_min_swaps_pairs(arr)
print(count, len(pairs))

