def pluck(arr):
    
    if not arr:
        return []
    smallest_even_value = float('inf')
    smallest_even_index = 0
    for i, value in enumerate(arr):
        if value % 2 == 0 and value < smallest_even_value:
            smallest_even_value = value
            smallest_even_index = i
    return [smallest_even_value, smallest_even_index]


if __name__ == '__main__':
    print(pluck([4, 2, 3]))
    print(pluck([1, 2, 3]))
    print