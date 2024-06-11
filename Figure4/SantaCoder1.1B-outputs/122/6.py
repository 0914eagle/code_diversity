def add_elements(arr, k):
    
    # TODO: Your code here
    arr.sort()
    return sum(arr[k - 1:k + 1])


