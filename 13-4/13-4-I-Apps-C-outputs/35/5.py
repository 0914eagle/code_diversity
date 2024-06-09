
import sys

def shortest_subarray_containing_all_numbers(arr, k):
    # Initialize a hash map to keep track of the numbers in the array
    num_map = {}
    for num in arr:
        if num not in num_map:
            num_map[num] = 1
        else:
            num_map[num] += 1
    
    # Initialize the shortest subarray length to the length of the array
    shortest_len = len(arr)
    
    # Iterate through the array and check if all numbers from 1 to k are present
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if len(num_map) == k:
                shortest_len = min(shortest_len, j - i + 1)
                break
            else:
                num_map[arr[j]] -= 1
                if num_map[arr[j]] == 0:
                    del num_map[arr[j]]
    
    # If all numbers from 1 to k are present, return the shortest subarray length
    # Otherwise, return -1
    if len(num_map) == 0:
        return shortest_len
    else:
        return -1

def change_value(arr, p, v):
    # Change the value of the p-th number in the array to v
    arr[p-1] = v
    return arr

if __name__ == '__main__':
    n, k, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(m):
        query = input().split()
        if query[0] == '1':
            # Change the value of a number in the array
            arr = change_value(arr, int(query[1]), int(query[2]))
        else:
            # Find the shortest subarray containing all numbers from 1 to k
            print(shortest_subarray_containing_all_numbers(arr, k))

