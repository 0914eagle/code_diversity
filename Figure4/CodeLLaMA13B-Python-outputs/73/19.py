def smallest_change(arr):
    
    if len(arr) < 2:
        return 0
    odd_count = 0
    odd_count_index = -1
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            odd_count += 1
            odd_count_index = i
    if odd_count == 0:
        return 0
    if odd_count == 1:
        return 1
    if odd_count % 2 == 0:
        return odd_count / 2
    if odd_count % 2 != 0:
        return (odd_count - 1) / 2 + 1


