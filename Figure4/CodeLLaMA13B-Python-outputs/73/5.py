def smallest_change(arr):
    
    if len(arr) < 2:
        return 0

    odds = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            odds += 1

    if odds > 1:
        return odds - 1
    return 0


if __name__ == "__main__":
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 2, 1]) == 0
