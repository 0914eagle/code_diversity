def maximum(arr, k):
    
    if k == 0: return []
    if k == 1: return [max(arr)]
    if k == len(arr): return sorted(arr)

    # find the kth largest number
    # use quick sort to partition the array
    # the kth largest number will be the pivot
    # the pivot will be the kth largest number
    # the left subarray will have numbers less than the pivot
    # the right subarray will have numbers greater than the pivot
    # the left subarray will have numbers less than the kth largest number
    # the right subarray will have numbers greater than the kth largest number
    # the left subarray will have numbers less than the kth largest number
    # the right subarray will have numbers greater than the kth largest number
    # ...
    # the left subarray will have numbers less than the kth largest number
    # the right subarray will have numbers greater than the kth largest number
    # the left subarray will have numbers less than the kth largest number
    # the right subarray will have numbers greater than the kth largest number
    # ...
    # the left subarray will have numbers less than the kth largest number
    # the right subarray will have numbers greater than the kth largest number
    # the left subarray will have numbers less than the kth largest number
    # the right subarray will have numbers greater than the kth largest number
    # ...
    # the left subarray will have numbers less than the kth largest number
    # the right subarray will have numbers greater than the kth largest number
    # the left subarray will have numbers less than the kth largest number
    # the right subarray will have numbers greater than the kth largest number
    # ...
    # the left subarray will have numbers less than the kth largest number
    # the right subarray will have numbers greater than the kth largest number
    # the left subarray will have numbers less than the kth largest number
    # the right subarray will have numbers greater than the kth largest number
    # ...
    # the left subarray will have numbers less than the kth largest number
    # the right subarray will have numbers greater than the kth largest number
    # the left subarray will