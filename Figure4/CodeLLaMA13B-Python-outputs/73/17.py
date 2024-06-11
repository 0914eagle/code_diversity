def smallest_change(arr):
    
    if len(arr) < 2:
        return 0

    odd_count = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            odd_count += 1

    if odd_count == 0:
        return 0
    if odd_count % 2 != 0:
        return odd_count

    # Find the first occurrence of odd number
    first_odd_index = -1
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            first_odd_index = i
            break

    # Find the last occurrence of odd number
    last_odd_index = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] % 2 != 0:
            last_odd_index = i
            break

    # If the first and last occurrence are adjacent, then we can't reduce the number of odd numbers
    if first_odd_index == last_odd_index - 1:
        return odd_count

    # If the first and last occurrence are not adjacent, then we can reduce the number of odd numbers
    # by swapping the first and last occurrence
    return odd_count - 2


if __name__ == "__main__":
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 10
    assert smallest_change([1, 2, 3, 4