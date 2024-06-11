def sort_array(arr):
    
    # Your code here
    return sorted(arr, key=lambda x: bin(x).count('1'))


