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
        return odd_count - 1
    return odd_count


if __name__ == "__main__":
    print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
    print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
    print(smallest_change([1, 2, 3, 2, 1]))
