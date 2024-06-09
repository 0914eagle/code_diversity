
import sys

def shortest_subarray(arr, k):
    # Initialize the hash map to keep track of the frequencies of each number
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Initialize the window start and end indices
    start, end = 0, 0
    min_len = len(arr) + 1
    while end < len(arr):
        # Add the current number to the hash map
        num = arr[end]
        freq[num] -= 1
        if freq[num] == 0:
            # If the frequency of the current number becomes 0, it means we have found a number that is not in the subarray
            del freq[num]
        
        # If the hash map is empty, it means we have found a subarray that contains all the numbers from 1 to k
        if len(freq) == 0:
            # Check if the length of the current subarray is less than the minimum length so far
            if end - start + 1 < min_len:
                min_len = end - start + 1
        
        # If the hash map has all the numbers from 1 to k, it means we have found a subarray that contains all the numbers from 1 to k
        if len(freq) == k:
            # Check if the length of the current subarray is less than the minimum length so far
            if end - start + 1 < min_len:
                min_len = end - start + 1
            # Move the window start index to the right to remove the numbers from the subarray
            while start <= end and arr[start] not in freq:
                freq[arr[start]] += 1
                if freq[arr[start]] > 0:
                    del freq[arr[start]]
                start += 1
        
        # Move the window end index to the right
        end += 1
    
    # If no subarray is found, return -1
    if min_len == len(arr) + 1:
        return -1
    else:
        return min_len

if __name__ == '__main__':
    n, k, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(m):
        query = input().split()
        if query[0] == '1':
            p, v = map(int, query[1:])
            arr[p-1] = v
        elif query[0] == '2':
            print(shortest_subarray(arr, k))

