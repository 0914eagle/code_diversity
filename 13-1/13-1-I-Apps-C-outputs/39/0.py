
def solve(arr, k, m):
    # Initialize a dictionary to store the frequency of each number
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Initialize a variable to store the length of the shortest contiguous subarray
    shortest_subarray = k + 1

    # Iterate through the queries
    for query in range(m):
        # If the query is of the first type, update the frequency of the number
        if arr[query][0] == 1:
            freq[arr[query][1]] += 1
        # If the query is of the second type, check if the shortest contiguous subarray exists
        elif arr[query][0] == 2:
            # Initialize a variable to store the length of the current subarray
            current_subarray = 0
            # Initialize a variable to store the start index of the current subarray
            start_index = 0
            # Iterate through the array
            for i in range(len(arr)):
                # If the current number is in the frequency dictionary and its frequency is greater than 0, increment the current subarray length
                if arr[i] in freq and freq[arr[i]] > 0:
                    freq[arr[i]] -= 1
                    current_subarray += 1
                # If the current subarray length is equal to the required length, update the start index
                if current_subarray == k:
                    start_index = i - k + 1
                    break
                # If the current subarray length is greater than the required length, break the loop
                elif current_subarray > k:
                    break
            # If the shortest subarray length is greater than the current subarray length, update the shortest subarray length and start index
            if current_subarray < shortest_subarray:
                shortest_subarray = current_subarray
                start_index = i - k + 1

    # Return the start index of the shortest subarray
    return start_index

