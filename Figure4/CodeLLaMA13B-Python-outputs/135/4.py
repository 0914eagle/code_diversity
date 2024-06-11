def can_arrange(arr):
    
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return i
    return -1


if __name__ == '__main__':
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    assert can_arrange([1, 2, 3]) == -1
    assert can_arrange([1, 2, 3, 4, 5]) == -1
    assert can_arrange([1, 2, 3, 4, 5, 6]) == -1
    assert can_arrange([1, 2, 3, 4, 5, 6, 7]) == -1
    assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8]) == -1
    assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
    assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == -1
    assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == -1
    assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == -1
    assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == -1
    assert can_arrange([1, 2, 3,