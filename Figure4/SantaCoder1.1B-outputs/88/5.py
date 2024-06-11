def sort_array(array):
    
    if len(array) <= 1:
        return array
    if sum(array) % 2 == 0:
        return sort_array(array[1:]) + array[0]
    return sort_array(array[1:]) + array[0]


if __name__ == '__main__':
    print(sort_array([5]))
    print(sort_array([2, 4, 3, 0, 1, 5]))
    print(sort_array([2, 4, 3, 0, 1, 5, 6]))
