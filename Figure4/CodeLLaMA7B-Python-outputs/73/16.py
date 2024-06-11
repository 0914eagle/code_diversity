def smallest_change(arr):
    
    if len(arr) <= 1:
        return 0

    # Find the middle of the array
    mid = len(arr) // 2

    # Reverse the second half of the array
    arr[mid:] = arr[mid:][::-1]

    # Count the number of differences between the two halves
    return sum(arr[i] != arr[~i] for i in range(mid))


