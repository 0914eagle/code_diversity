def add_elements(arr, k):
    
    # Time O(n) | Space O(1)
    total = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            total += arr[i]
    return total

