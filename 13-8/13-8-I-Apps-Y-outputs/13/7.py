
def solve(arr):
    n = len(arr)
    if n % 6 == 0:
        return 0
    
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize variables to keep track of the number of elements to remove
    remove = 0
    count = 0
    
    # Iterate through the array and count the number of occurrences of each number
    for i in range(n):
        if arr[i] == 4:
            count += 1
        elif arr[i] == 8:
            count += 2
        elif arr[i] == 15:
            count += 3
        elif arr[i] == 16:
            count += 4
        elif arr[i] == 23:
            count += 5
        elif arr[i] == 42:
            count += 6
    
    # If the count is not a multiple of 6, remove the minimum number of elements to make it a multiple of 6
    if count % 6 != 0:
        remove = 6 - (count % 6)
    
    return remove

