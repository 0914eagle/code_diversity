

def smallest_change(arr):
    
    # Step 1: Reverse the array
    rev_arr = arr[::-1]

    # Step 2: Find the first index where the array and its reverse differ
    for i in range(len(arr)):
        if arr[i] != rev_arr[i]:
            # If the first index is found, check if the remaining elements are a palindrome
            if arr[i+1:] == rev_arr[i+1:]:
                return 1
            else:
                # If the remaining elements are not a palindrome, find the minimum number of elements to change
                min_changes = float('inf')
                for j in range(i+1, len(arr)):
                    if arr[j] == rev_arr[j]:
                        continue
                    else:
                        min_changes = min(min_changes, 2)
                return min_changes + 1

    # If the array is already a palindrome, return 0
    return 0


