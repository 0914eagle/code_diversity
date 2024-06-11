def sort_array(array):
    
    if len(array) <= 1:
        return array
    if len(array) == 2:
        if array[0] > array[1]:
            return [array[1], array[0]]
        else:
            return [array[0], array[1]]
    if len(array) % 2 == 0:
        return sort_array(array[0:len(array) // 2]) + sort_array(array[len(array) // 2:])
    else:
        return sort_array(array[0:len(array) // 2]) + sort_array(array[len(array) // 2 + 1:])


if __name__ == '__main__':
    print(sort_array([5, 2, 4, 3, 0, 1, 5, 6]))
    print(sort_array([2, 4, 3, 0, 1, 5]))
    print(sort_array([2, 4, 3, 0, 1, 5, 6]))
