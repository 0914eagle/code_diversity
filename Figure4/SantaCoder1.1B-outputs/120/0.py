def maximum(arr, k):
    
    if k == 1:
        return arr
    if k == 2:
        return max(arr) if arr[0] > arr[1] else min(arr)
    if k == 3:
        return max(arr) if arr[0] > arr[1] else min(arr) if arr[0] > arr[2] else arr[0]
    if k == 4:
        return max(arr) if arr[0] > arr[1] else min(arr) if arr[0] > arr[2] else min(arr) if arr[1] > arr[2] else arr[0]
    if k == 5:
        return max(arr) if arr[0] > arr[1] else min(arr) if arr[0] > arr[2] else min(arr) if arr[1] > arr[2] else min(arr) if arr[0] > arr[1] else arr[0]
    if k == 6:
        return max(arr) if arr[0] > arr[1] else min(arr) if arr[0] > arr[2] else min(arr) if arr[1] > arr[2] else min(arr) if arr[0] > arr[1] else min(arr) if arr[1] > arr[2] else arr[0]
    if k == 7:
        return max(arr) if arr[0] > arr[1] else min(arr) if arr[0] > arr[2] else min(arr) if arr[1] > arr[2] else min(arr) if arr[0] > arr[1] else min(arr) if arr[1] > arr[2] else min(arr) if arr[0] > arr[1] else arr[0]
    if k == 8:
        return max(arr) if arr[0] > arr[1] else min(arr) if arr[0] > arr[2] else min(arr) if arr[1] > arr[2] else min(arr) if arr[0] > arr[1] else min(arr) if arr[1] > arr[2] else min(arr) if arr[0] > arr[1] else min(arr) if arr[1] >