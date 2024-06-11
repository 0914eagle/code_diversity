def maximum(arr, k):
    
    if not arr or k <= 0:
        return []

    # sort the array
    arr.sort()

    # return the last k elements
    return arr[-k:]


