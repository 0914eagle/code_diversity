def can_arrange(arr):
    
    # Your code here
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return i
    return -1


if