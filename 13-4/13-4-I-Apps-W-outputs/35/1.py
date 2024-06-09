
def swap_elements(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def count_swaps(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
                swap_elements(arr, i, j)
    return count

def get_min_swaps(arr):
    n = len(arr)
    min_swaps = count_swaps(arr)
    min_pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                swap_elements(arr, i, j)
                swaps = count_swaps(arr)
                if swaps < min_swaps:
                    min_swaps = swaps
                    min_pairs = [(i, j)]
                elif swaps == min_swaps:
                    min_pairs.append((i, j))
                swap_elements(arr, i, j)
    return min_swaps, len(min_pairs)

n = int(input())
arr = list(map(int, input().split()))
min_swaps, min_pairs = get_min_swaps(arr)
print(min_swaps, min_pairs)

