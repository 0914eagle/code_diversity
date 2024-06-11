def maximum(arr, k):
    
    if k == 0:
        return []

    # find the kth largest number in arr
    # use quick sort to partition the array
    # return the first k numbers in the right part
    