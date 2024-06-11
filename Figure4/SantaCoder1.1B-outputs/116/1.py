def sort_array(arr):
    
    # Your code here
    return sorted(arr, key=lambda x: x.count('1'))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
