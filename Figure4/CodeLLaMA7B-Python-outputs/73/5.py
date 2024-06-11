def smallest_change(arr):
    
    # Your code here
    # 1. Find the middle of the array
    # 2. Reverse the second half of the array
    # 3. Iterate through the array and count the number of differences
    # 4. Return the minimum number of differences
    middle = len(arr) // 2
    arr_reversed = arr[middle:]
    arr_reversed.reverse()
    diff = 0
    for i in range(len(arr)):
        if arr[i] != arr_reversed[i]:
            diff += 1
    return diff


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
