
import sys

def shortest_subarray(arr, k):
    # Initialize the shortest subarray length to the size of the array
    shortest_len = len(arr)
    # Initialize a set to keep track of the numbers in the array
    nums = set(arr)
    # Iterate through the array
    for i in range(len(arr)):
        # If the current number is not in the set, skip it
        if arr[i] not in nums:
            continue
        # If the current number is in the set, calculate the length of the subarray starting from this index
        subarray_len = 1
        # Iterate through the rest of the array
        for j in range(i+1, len(arr)):
            # If the current number is not in the set, break the inner loop
            if arr[j] not in nums:
                break
            # If the current number is in the set, increment the subarray length
            subarray_len += 1
        # If the subarray length is shorter than the current shortest length, update the shortest length
        if subarray_len < shortest_len:
            shortest_len = subarray_len
    # Return the shortest length
    return shortest_len

def change_value(arr, p, v):
    # Change the value of the p-th number to v
    arr[p-1] = v
    return arr

def main():
    # Read the input
    n, k, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # Iterate through the queries
    for i in range(m):
        # Read the query
        query = input().split()
        # If the query is of the first type, change the value of the p-th number to v
        if query[0] == "1":
            arr = change_value(arr, int(query[1]), int(query[2]))
        # If the query is of the second type, find the shortest subarray containing all numbers from 1 to k
        elif query[0] == "2":
            print(shortest_subarray(arr, k))
        # If the query is of a different type, print an error message
        else:
            print("Invalid query")

if __name__ == "__main__":
    main()

