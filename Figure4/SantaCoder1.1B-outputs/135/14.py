def can_arrange(arr):
    
    if len(arr) < 2:
        return -1
    else:
        for i in range(len(arr)):
            if arr[i] > arr[i-1]:
                return i
        return -1


