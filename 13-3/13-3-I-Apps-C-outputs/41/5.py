
def count_scary_subarrays(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    median = sorted_arr[n//2] if n % 2 == 1 else (sorted_arr[n//2] + sorted_arr[n//2-1]) / 2
    count = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] == median:
                count += 1
    return count

