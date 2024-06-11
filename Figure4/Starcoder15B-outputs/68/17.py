def pluck(arr):
    
    if not arr:
        return []
    min_even = float('inf')
    min_even_index = 0
    for i, v in enumerate(arr):
        if v < min_even and v % 2 == 0:
            min_even = v
            min_even_index = i
    return [min_even, min_even_index]


if __name__ == '__main__':
    assert pluck([4, 2