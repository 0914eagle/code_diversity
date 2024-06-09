
import sys

def shortest_subarray(arr, k):
    # Initialize the shortest subarray length to the size of the array
    shortest_len = len(arr)
    # Initialize the current subarray length to 0
    current_len = 0
    # Initialize the set of numbers in the subarray
    nums = set()
    
    for num in arr:
        # If the number is not in the subarray, add it and increment the current subarray length
        if num not in nums:
            nums.add(num)
            current_len += 1
        # If the number is in the subarray, remove it and decrement the current subarray length
        else:
            nums.remove(num)
            current_len -= 1
        
        # If the current subarray length is equal to the required length, update the shortest subarray length
        if current_len == k:
            shortest_len = min(shortest_len, current_len)
        
        # If the current subarray length is greater than the required length, break the loop
        if current_len > k:
            break
    
    # Return the shortest subarray length
    return shortest_len

def main():
    # Read the input data from stdin
    n, k, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Loop through the queries
    for i in range(m):
        # Read the query type and parameters
        query = input().split()
        qtype = int(query[0])
        if qtype == 1:
            # Change the value of the p-th number to v
            p, v = map(int, query[1:])
            arr[p-1] = v
        elif qtype == 2:
            # Find the length of the shortest subarray containing all numbers from 1 to k
            print(shortest_subarray(arr, k))
        else:
            print("Invalid query type")

if __name__ == "__main__":
    main()

