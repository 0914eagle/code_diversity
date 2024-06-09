
import sys

def shortest_subarray(arr, k):
    # Initialize the variables
    start = 0
    end = 0
    count = [0] * (k+1)
    min_len = float('inf')
    curr_len = 0

    # Iterate through the array
    for end in range(len(arr)):
        count[arr[end]] += 1
        curr_len = count[arr[end]]
        while count[arr[start]] > 1:
            count[arr[start]] -= 1
            start += 1
        min_len = min(min_len, curr_len)

    # Return the result
    if min_len == float('inf'):
        return -1
    else:
        return min_len

# Main function
if __name__ == '__main__':
    # Read the input
    n, k, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    for i in range(m):
        queries.append(list(map(int, input().split())))

    # Process the queries
    for query in queries:
        if query[0] == 1:
            arr[query[1]-1] = query[2]
        else:
            print(shortest_subarray(arr, k))


