def sort_array(arr):
    
    return sorted(arr, key=lambda x: int(bin(x)[2:], 2))


