def add_elements(arr, k):
    
    # O(n) time, O(1) space
    total = 0
    for i in range(k):
        total += arr[i]
        if len(str(arr[i])) > 2:
            break
    return total


