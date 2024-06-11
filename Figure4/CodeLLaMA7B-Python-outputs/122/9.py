def add_elements(arr, k):
    
    # O(n) time, O(1) space
    sum = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum += arr[i]
    return sum


