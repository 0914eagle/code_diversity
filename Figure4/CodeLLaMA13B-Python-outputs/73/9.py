def smallest_change(arr):
    
    if len(arr) <= 1:
        return 0

    odd_count = 0
    odd_positions = []
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            odd_count += 1
            odd_positions.append(i)

    if odd_count == 0:
        return 0
    if odd_count % 2 != 0:
        return len(arr) - odd_count

    if odd_count == 2:
        return 2

    return 2 + min(abs(odd_positions[0] - odd_positions[1]), abs(odd_positions[1] - odd_positions[2]))


if __name__ == "__main__":
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 2, 1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 