
import sys

def shortest_subarray_length(arr, k):
    # Initialize the hash map to keep track of the frequencies of each number
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Initialize the minimum length of the subarray
    min_len = len(arr) + 1
    
    # Iterate through the hash map and check if all numbers from 1 to k are present
    for i in range(1, k+1):
        if i not in freq:
            return -1
    
    # If all numbers are present, iterate through the array and check for the minimum length of the subarray
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if len(freq) == k:
                min_len = min(min_len, j - i + 1)
                break
            freq[arr[j]] -= 1
            if freq[arr[j]] == 0:
                del freq[arr[j]]
    
    return min_len

def change_value(arr, p, v):
    arr[p-1] = v

if __name__ == '__main__':
    n, k, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for i in range(m):
        query = input().split()
        if query[0] == '1':
            change_value(arr, int(query[1]), int(query[2]))
        else:
            print(shortest_subarray_length(arr, k))


