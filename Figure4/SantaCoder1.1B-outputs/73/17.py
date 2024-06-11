def smallest_change(arr):
    
    # Write your code here.
    # return len(arr)
    # return min(len(arr), min(len(arr) // 2, min(arr) // 2))
    return min(len(arr), min(len(arr) // 2, min(arr) // 2, min(arr) // 2))


