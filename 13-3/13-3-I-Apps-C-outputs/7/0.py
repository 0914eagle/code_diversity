
def longest_consecutive_subarray(arr):
    # Sort the array
    arr.sort()
    # Initialize variables to keep track of the longest subarray length and the current subarray length
    longest, current = 0, 0
    # Iterate through the array
    for i in range(len(arr)):
        # If the current element is the same as the previous element, increment the current subarray length
        if i > 0 and arr[i] == arr[i-1]:
            current += 1
        # If the current element is different from the previous element, reset the current subarray length
        else:
            current = 1
        # Update the longest subarray length if the current subarray length is greater than the longest subarray length
        longest = max(longest, current)
    return longest

