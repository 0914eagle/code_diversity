
def solve(arr, k, m):
    # Initialize a dictionary to store the frequency of each number
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Initialize a variable to store the length of the shortest contiguous subarray
    shortest_subarray = len(arr) + 1

    # Iterate through the queries
    for query in range(m):
        # If the query is of the first type, update the frequency of the number
        if arr[query][0] == 1:
            freq[arr[query][1]] -= 1
            freq[arr[query][2]] += 1
        # If the query is of the second type, find the length of the shortest contiguous subarray
        elif arr[query][0] == 2:
            # Initialize a variable to store the current length of the subarray
            curr_subarray = 0
            # Initialize a variable to store the start index of the subarray
            start_index = 0
            # Iterate through the array
            for i in range(len(arr)):
                # If the current number is in the frequency dictionary and its frequency is greater than 0, increment the current length of the subarray
                if arr[i] in freq and freq[arr[i]] > 0:
                    curr_subarray += 1
                # If the current length of the subarray is equal to k, update the length of the shortest contiguous subarray
                if curr_subarray == k:
                    shortest_subarray = min(shortest_subarray, i - start_index + 1)
                # If the current length of the subarray is greater than k, update the start index of the subarray and reset the current length of the subarray
                if curr_subarray > k:
                    start_index = i - curr_subarray + 1
                    curr_subarray = 0
            # If the current length of the subarray is equal to k, update the length of the shortest contiguous subarray
            if curr_subarray == k:
                shortest_subarray = min(shortest_subarray, len(arr) - start_index + 1)

    # Return the length of the shortest contiguous subarray
    return shortest_subarray

