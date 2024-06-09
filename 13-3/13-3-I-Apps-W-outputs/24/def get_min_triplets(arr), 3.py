
def get_min_triplets(arr):
    arr.sort()
    count = 0
    for i in range(len(arr)-2):
        j = i+1
        k = len(arr)-1
        while j < k:
            if arr[i] * arr[j] * arr[k] < arr[i] * arr[k] * arr[j]:
                count += 1
                j += 1
            else:
                k -= 1
    return count

