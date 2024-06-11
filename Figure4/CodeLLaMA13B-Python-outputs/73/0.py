def smallest_change(arr):
    
    if len(arr) <= 1:
        return 0
    if len(arr) == 2:
        return 1
    odd = 0
    even = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            if arr[i] != arr[i + 1]:
                even += 1
        else:
            if arr[i] != arr[i - 1]:
                odd += 1
    return min(even, odd)


if __name__ == "__main__":
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 2, 1]) == 0
