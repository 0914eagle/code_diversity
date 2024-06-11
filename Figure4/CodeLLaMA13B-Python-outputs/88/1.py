def sort_array(array):
    
    if len(array) == 0:
        return array
    else:
        return sorted(array, key=lambda x: x, reverse=sum(array[:2]) % 2 == 0)


