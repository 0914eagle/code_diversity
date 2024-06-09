
def solve(arr, k, m):
    # Initialize a dictionary to store the frequency of each number
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Initialize a variable to store the length of the shortest subarray
    shortest_subarray = len(arr) + 1

    # Loop through the queries
    for query in range(m):
        # If the query is of the first type, update the frequency of the number
        if arr[query][0] == 1:
            freq[arr[query][1]] -= 1
            freq[arr[query][2]] += 1
        # If the query is of the second type, check if the subarray exists
        elif arr[query][0] == 2:
            # Initialize a variable to store the length of the current subarray
            current_subarray = 0
            # Initialize a variable to store the start index of the current subarray
            start_index = 0
            # Loop through the array
            for i in range(len(arr)):
                # If the current number is in the frequency dictionary and its frequency is greater than 0, increment the current subarray length
                if arr[i] in freq and freq[arr[i]] > 0:
                    current_subarray += 1
                # If the current subarray length is equal to k, check if it is the shortest subarray
                if current_subarray == k:
                    shortest_subarray = min(shortest_subarray, i - start_index + 1)
                    start_index = i + 1
                    current_subarray = 0
            # If the current subarray length is equal to k, check if it is the shortest subarray
            if current_subarray == k:
                shortest_subarray = min(shortest_subarray, len(arr) - start_index)

    # Return the length of the shortest subarray
    return shortest_subarray

