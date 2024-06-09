
def max_sum_after_k_swaps(arr, k):
    n = len(arr)
    def sum_subarray(l, r):
        return sum(arr[l:r+1])
    
    def max_subarray_sum(l, r):
        if l > r:
            return 0
        max_sum = sum_subarray(l, r)
        for i in range(l, r):
            max_sum = max(max_sum, max_subarray_sum(l, i) + max_subarray_sum(i+1, r))
        return max_sum
    
    for i in range(k):
        max_sum = max_subarray_sum(0, n-1)
        for j in range(n-1):
            for i in range(n-j-1):
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    max_sum = max(max_sum, max_subarray_sum(0, n-1))
                    break
    
    return max_sum

