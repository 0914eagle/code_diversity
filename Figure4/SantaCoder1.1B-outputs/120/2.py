def maximum(arr, k):
    
    # Sort the array
    arr.sort()

    # Return the k largest elements
    return arr[-k:]


if