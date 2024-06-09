
def count_scary_subarrays(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] == sorted(arr[i:j+1])[len(arr[i:j+1])//2]:
                count += 1
    return count

