

def smallest_change(arr):
    
    # Step 1: Reverse the array
    rev_arr = arr[::-1]

    # Step 2: Find the first index where the array and its reverse differ
    for i in range(len(arr)):
        if arr[i] != rev_arr[i]:
            # If the first difference is at index i, then the minimum number of changes required is len(arr) - i
            return len(arr) - i

    # If the array is already palindromic, then the minimum number of changes required is 0
    return 0


