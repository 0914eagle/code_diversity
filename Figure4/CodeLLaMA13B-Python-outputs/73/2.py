def smallest_change(arr):
    
    if len(arr) <= 1:
        return 0
    if len(arr) == 2:
        return 1
    # O(n)
    left = 0
    right = len(arr) - 1
    count = 0
    while left < right:
        if arr[left] != arr[right]:
            count += 1
            if arr[left] == arr[right - 1]:
                right -= 1
            elif arr[left + 1] == arr[right]:
                left += 1
            else:
                return -1
        else:
            left += 1
            right -= 1
    return count


if __name__ == "__main__":
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 1
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9,