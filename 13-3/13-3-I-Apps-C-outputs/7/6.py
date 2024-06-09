
def longest_consecutive_subarray(arr):
    # Sort the array
    arr.sort()
    # Initialize variables to keep track of the longest subarray length and its start index
    longest, start = 0, 0
    # Iterate through the array
    for i in range(len(arr)):
        # If the current element is already visited, skip it
        if arr[i] in arr[:i]:
            continue
        # If the current element is not visited, start a new subarray
        start = i
        # Keep track of the length of the subarray
        length = 1
        # Iterate through the remaining elements in the array
        for j in range(i+1, len(arr)):
            # If the current element is not visited and is adjacent to the previous element, add it to the subarray
            if arr[j] not in arr[:j] and arr[j] == arr[j-1] + 1:
                length += 1
            # If the current element is not visited and is not adjacent to the previous element, break the subarray
            else:
                break
        # Update the longest subarray length if the current subarray is longer
        longest = max(longest, length)
    return longest

