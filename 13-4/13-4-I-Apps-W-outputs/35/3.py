
def swap_elements(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                count += 1
    return count

def find_min_swaps(arr):
    n = len(arr)
    min_count = float('inf')
    min_pairs = []
    for i in range(n):
        for j in range(i+1, n):
            tmp = arr[:]
            tmp[i], tmp[j] = tmp[j], tmp[i]
            count = swap_elements(tmp)
            if count < min_count:
                min_count = count
                min_pairs = [(i, j)]
            elif count == min_count:
                min_pairs.append((i, j))
    return min_count, len(min_pairs)

n = int(input())
arr = list(map(int, input().split()))
count, pairs = find_min_swaps(arr)
print(count, pairs)

