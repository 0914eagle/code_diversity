def add_elements(arr, k):
    
    # O(n) time, O(1) space
    if k == 0:
        return 0
    elif k == 1:
        return sum(arr)
    else:
        return sum(arr[:k]) - sum(arr[:k-1])
