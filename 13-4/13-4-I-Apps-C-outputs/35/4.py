
import sys

def shortest_subarray(arr, k):
    # Initialize the window start and end indices
    start, end = 0, 0
    # Initialize the count of unique elements in the window
    count = 0
    # Initialize the minimum length of the subarray
    min_len = float('inf')
    # Loop through the array
    while end < len(arr):
        # Add the current element to the window
        if arr[end] in range(1, k+1):
            count += 1
        # Remove the first element from the window if it is not in the range
        if arr[start] not in range(1, k+1):
            count -= 1
        # If the window has all unique elements, check if the length is less than the minimum length
        if count == k:
            min_len = min(min_len, end - start + 1)
        # Move the window forward
        end += 1
        # Move the window backward if the window has more unique elements than required
        while count > k:
            if arr[start] in range(1, k+1):
                count -= 1
            start += 1
    # Return the minimum length
    if min_len == float('inf'):
        return -1
    else:
        return min_len

def change_value(arr, p, v):
    # Change the value of the p-th element to v
    arr[p-1] = v
    return arr

# Read the input
N, K, M = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(M):
    # Read the query
    query = input().split()
    # If the query is to change a value, change the value and update the array
    if query[0] == '1':
        arr = change_value(arr, int(query[1]), int(query[2]))
    # If the query is to find the shortest subarray, find the shortest subarray and print the result
    elif query[0] == '2':
        print(shortest_subarray(arr, K))


