

def smallest_change(arr):
    
    # Step 1: Reverse the array
    reversed_arr = arr[::-1]

    # Step 2: Find the first index where the array and its reverse differ
    for i in range(len(arr)):
        if arr[i] != reversed_arr[i]:
            # If the first index is found, check if the remaining elements are the same
            if arr[i+1:] == reversed_arr[i+1:]:
                return 1
            else:
                # If the remaining elements are not the same, find the first index where they differ
                for j in range(i+1, len(arr)):
                    if arr[j] != reversed_arr[j]:
                        return j - i + 1

    # If the array and its reverse are the same, no changes need to be made
    return 0


