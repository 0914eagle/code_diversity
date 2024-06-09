
import sys

def shortest_subarray(arr, k):
    # Initialize the shortest subarray length to the size of the array
    shortest = len(arr)
    # Initialize a set to keep track of the numbers in the array
    nums = set(arr)
    # Iterate through the array
    for i in range(len(arr)):
        # If the current number is not in the set, skip it
        if arr[i] not in nums:
            continue
        # If the current number is in the set, remove it from the set
        nums.remove(arr[i])
        # If the set is empty, we have found a subarray containing all numbers from 1 to k
        if not nums:
            # Update the shortest subarray length
            shortest = min(shortest, i+1)
            # Break out of the loop
            break
    # Return the shortest subarray length
    return shortest

def change_value(arr, p, v):
    # Change the value of the p-th number to v
    arr[p-1] = v
    # Return the modified array
    return arr

# Read the input
N, K, M = map(int, input().split())
arr = list(map(int, input().split()))

# Iterate through the queries
for i in range(M):
    # Read the query type and parameters
    query = input().split()
    # If the query is to change a value
    if query[0] == "1":
        # Change the value of the p-th number to v
        arr = change_value(arr, int(query[1]), int(query[2]))
    # If the query is to find the shortest subarray
    elif query[0] == "2":
        # Find the shortest subarray containing all numbers from 1 to k
        shortest = shortest_subarray(arr, K)
        # Print the result
        print(shortest if shortest != len(arr) else -1)


