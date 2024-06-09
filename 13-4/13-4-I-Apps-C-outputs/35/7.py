
import sys

def shortest_subarray(arr, k):
    # Initialize the shortest subarray length to the size of the array
    shortest_len = len(arr)
    # Initialize the current subarray length to 0
    curr_len = 0
    # Initialize the current subarray start index to 0
    start_idx = 0
    # Initialize a set to keep track of the numbers in the subarray
    nums = set()

    # Iterate through the array
    for i in range(len(arr)):
        # If the current number is in the subarray, increment the current subarray length
        if arr[i] in nums:
            curr_len += 1
        # If the current number is not in the subarray, reset the current subarray length and start index
        else:
            curr_len = 1
            start_idx = i
        # Add the current number to the set
        nums.add(arr[i])
        # If the current subarray length is equal to the required length, update the shortest subarray length and break
        if curr_len == k:
            shortest_len = min(shortest_len, i - start_idx + 1)
            break

    # If the shortest subarray length is equal to the size of the array, it means that no subarray of the required length exists
    if shortest_len == len(arr):
        return -1
    else:
        return shortest_len

def change_value(arr, p, v):
    arr[p-1] = v

if __name__ == '__main__':
    n, k, m = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(m):
        query = input().split()
        if query[0] == '1':
            change_value(arr, int(query[1]), int(query[2]))
        elif query[0] == '2':
            print(shortest_subarray(arr, k))


