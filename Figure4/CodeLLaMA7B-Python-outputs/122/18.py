def add_elements(arr, k):
    
    # Time O(n) | Space O(1)
    total = 0
    for i in range(k):
        total += arr[i]
    return total


