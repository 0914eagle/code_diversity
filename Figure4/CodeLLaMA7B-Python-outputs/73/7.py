def smallest_change(arr):
    
    # Your code here
    # 1. Find the middle of the array
    # 2. Reverse the second half
    # 3. Iterate through the array and count the number of differences
    # 4. Return the minimum number of differences

    # 1. Find the middle of the array
    middle = len(arr) // 2
    # 2. Reverse the second half
    arr[middle:] = arr[middle:][::-1]
    # 3. Iterate through the array and count the number of differences
    count = 0
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - 1 - i]:
            count += 1
    return count


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
