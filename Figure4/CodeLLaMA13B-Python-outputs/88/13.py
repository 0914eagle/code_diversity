def sort_array(array):
    
    if not array:
        return array
    if len(array) == 1:
        return array
    else:
        if sum(array[0], array[-1]) % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)


if __name__ == '__main__':
    assert sort_array([]) == []
    assert sort_array([5]) == [5]
    assert sort_array([2, 4, 3, 0