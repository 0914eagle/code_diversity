

def smallest_change(arr):
    
    # Step 1: Reverse the array
    reversed_arr = arr[::-1]

    # Step 2: Find the first index where the array and its reverse differ
    first_diff_index = 0
    for i in range(len(arr)):
        if arr[i] != reversed_arr[i]:
            first_diff_index = i
            break

    # Step 3: Count the number of elements that need to be changed
    num_changes = 0
    for i in range(first_diff_index, len(arr)):
        if arr[i] != reversed_arr[i]:
            num_changes += 1

    return num_changes


