def sort_array(arr):
    
    # Your code here
    return sorted(arr, key=lambda x: int(bin(x)[2:], 2))


