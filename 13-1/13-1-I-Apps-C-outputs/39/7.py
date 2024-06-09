
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
        # If the current number is in the set, calculate the length of the subarray
        length = 1
        # Iterate through the rest of the array
        for j in range(i+1, len(arr)):
            # If the current number is not in the set, break the inner loop
            if arr[j] not in nums:
                break
            # If the current number is in the set, increment the length of the subarray
            length += 1
        # If the length of the subarray is shorter than the current shortest subarray, update the shortest subarray length
        if length < shortest:
            shortest = length
    # Return the shortest subarray length
    return shortest

def change_value(arr, p, v):
    # Change the value of the p-th number in the array to v
    arr[p-1] = v
    # Return the updated array
    return arr

def main():
    # Read the input
    N, K, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # Iterate through the queries
    for i in range(M):
        # Read the query
        query = input().split()
        # If the query is to change a value, change the value and update the array
        if query[0] == "1":
            arr = change_value(arr, int(query[1]), int(query[2]))
        # If the query is to find the shortest subarray, find the shortest subarray and print the result
        elif query[0] == "2":
            print(shortest_subarray(arr, K))

if __name__ == "__main__":
    main()

