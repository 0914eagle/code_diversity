
def longest_consecutive_subarray(arr):
    # Sort the array
    arr.sort()
    # Initialize variables to keep track of the longest subarray length and its start index
    longest, start = 0, 0
    # Iterate through the array
    for i in range(len(arr)):
        # If the current element is not the next element in the subarray, start a new subarray
        if i == 0 or arr[i] != arr[i-1] + 1:
            start = i
        # If the current element is the next element in the subarray, update the subarray length
        if arr[i] == arr[start] + (i - start):
            longest = max(longest, i - start + 1)
    return longest

