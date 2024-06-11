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

    # O(n)
    left_half = arr[: len(arr) // 2]
    right_half = arr[len(arr) // 2 :]
    right_half.reverse()

    # O(n)
    left_counter = Counter(left_half)
    right_counter = Counter(right_half)

    # O(n)
    left_keys = set(left_counter.keys())
    right_keys = set(right_counter.keys())

    # O(n)
    diff_keys = left_keys.symmetric_difference(right_keys)

    # O(n)
    return sum(
        [
            abs(left_counter[key] - right_counter[key])
            for key in diff_keys
            if key in left_counter
        ]
        + [
            abs(left_counter[key] - right_counter[key])
            for key in diff_keys
            if key in right_counter
        ]
    )


if __name__ == "__main__":
    print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
    print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
    print(smallest_change([1, 2, 3, 2, 1]))
