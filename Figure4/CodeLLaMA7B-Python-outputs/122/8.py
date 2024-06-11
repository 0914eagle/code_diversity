def add_elements(arr, k):
    
    # O(n) time, O(1) space
    total = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            total += arr[i]
    return total


