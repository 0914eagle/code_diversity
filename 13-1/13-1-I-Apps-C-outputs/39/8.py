
def solve(arr, queries):
    # Initialize a dictionary to keep track of the frequencies of each number
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Iterate through the queries
    for query in queries:
        # If the query is of type 1, update the frequency of the number at index p to v
        if query[0] == 1:
            p, v = query[1], query[2]
            freq[arr[p-1]] -= 1
            arr[p-1] = v
            freq[v] += 1
        # If the query is of type 2, find the length of the shortest contiguous subarray containing all numbers from 1 to K
        else:
            # Initialize a variable to keep track of the minimum length
            min_len = float('inf')
            # Iterate through the frequencies
            for num in range(1, K+1):
                # If the frequency of the current number is non-zero, update the minimum length
                if freq[num] > 0:
                    min_len = min(min_len, freq[num])
            # If the minimum length is infinity, there is no subarray containing all numbers from 1 to K, so output -1
            if min_len == float('inf'):
                print(-1)
            # Otherwise, output the minimum length
            else:
                print(min_len)

# Test the function with some examples
arr = [2, 3, 1, 2]
queries = [[1, 3, 3], [2], [1, 1, 1], [2]]
solve(arr, queries)

arr = [3, 2, 1, 4]
queries = [[1, 2, 3], [2], [1, 1, 1], [2]]
solve(arr, queries)

