def smallest_change(arr):
    
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 1

    odd_count = 0
    even_count = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            if arr[i] != arr[len(arr) - 1 - i]:
                even_count += 1
        else:
            if arr[i] != arr[len(arr) - 1 - i]:
                odd_count += 1

    if odd_count == 0:
        return even_count
    else:
        return min(odd_count, even_count)


if __name__ == "__main__":
    assert smallest_change([1,2,3,5,4,7,9,6]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 2, 1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 2, 1,