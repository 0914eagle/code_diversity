def maximum(arr, k):
    
    # sort the array
    arr.sort()
    # return the maximum k elements
    return arr[-k:]


