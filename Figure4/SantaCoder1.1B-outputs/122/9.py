def add_elements(arr, k):
    
    if len(arr) < k:
        return 0
    return sum(arr[:k]) + sum(arr[k:])


