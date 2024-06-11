def add_elements(arr, k):
    
    # Edge case
    if len(arr) < k:
        return 0

    # Initialize result
    result = 0

    # Iterate through the array
    for i in range(k):
        # Add the element to the result
        result += arr[i]

    # Return the result
    return result


if __name__ == "__main__":
    # Test 1
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 4
    expected = 24
    actual = add_elements(arr, k)
    assert expected == actual

    # Test 2
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 5
    expected = 24
    actual = add_elements(arr, k)
    assert expected == actual

    # Test 3
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 6
    expected = 24
    actual = add_elements(arr, k)
    assert expected == actual

    # Test 4
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 7
    expected = 24
    actual = add_elements(arr, k)
    assert expected == actual

    # Test 5
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 8
    expected = 24
    actual = add_elements(arr, k)
    assert expected == actual

    # Test 6
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 9
    expected = 24
    actual = add_elements(arr, k)
    assert expected == actual
