def sort_array(array):
    
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return [array[0]]
    else:
        if sum(array[0], array[-1]) % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)


if __name__ == '__main__':
    print("Example:")
    print(list(sort_array([2, 4, 3, 0, 