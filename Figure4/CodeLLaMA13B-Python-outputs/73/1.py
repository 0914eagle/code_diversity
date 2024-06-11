def smallest_change(arr):
    
    if not arr:
        return 0

    odd_count = 0
    odd_indices = []
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            odd_count += 1
            odd_indices.append(i)

    if odd_count == 0:
        return 0
    if odd_count % 2 != 0:
        return len(arr) - odd_count + 1

    odd_indices.sort()
    return min(odd_indices[i + 1] - odd_indices[i] for i in range(0, len(odd_indices) - 1, 2))


if __name__ == "__main__":
    assert smallest_change([1,2,3,5,4,7,9,6]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 2, 1]) == 0
