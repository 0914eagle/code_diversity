def sort_array(arr):
    
    return sorted(arr, key=lambda x: (x.count('1'), int(x, 2)))


