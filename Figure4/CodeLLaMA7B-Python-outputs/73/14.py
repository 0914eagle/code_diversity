def smallest_change(arr):
    
    # TODO: Write your code here
    # 1. Find the middle of the array
    # 2. Reverse the second half
    # 3. Count the number of differences
    # 4. Return the number of differences
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 1 if arr[0] != arr[1] else 0
    if len(arr) == 3:
        return 2 if arr[0] != arr[2] else 1

    middle = len(arr) // 2
    first_half = arr[:middle]
    second_half = arr[middle:]
    second_half.reverse()

    diffs = 0
    for i in range(len(first_half)):
        if first_half[i] != second_half[i]:
            diffs += 1

    return diffs


