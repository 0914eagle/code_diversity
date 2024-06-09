
def count_scary_subarrays(arr):
    n = len(arr)
    scary_subarrays = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] == sorted(arr[i:j+1])[len(arr[i:j+1])//2]:
                scary_subarrays += 1
    return scary_subarrays

