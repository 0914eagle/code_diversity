
def get_minimum_triples(arr):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n-2):
        j = i+1
        k = n-1
        while j < k:
            if arr[i] * arr[j] * arr[k] < arr[i] * arr[k] * arr[j]:
                count += 1
                j += 1
            else:
                k -= 1
    return count

