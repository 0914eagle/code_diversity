def add_elements(arr, k):
    
    # O(n) time, O(1) space
    if k == 0:
        return 0
    if k == 1:
        return sum(arr)
    if k == len(arr):
        return sum(arr)

    total = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            total += arr[i]
    return total


