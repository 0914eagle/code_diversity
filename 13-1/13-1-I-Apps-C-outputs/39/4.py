
def solve(arr, queries):
    # Initialize a dictionary to keep track of the frequencies of each number
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Iterate through the queries
    for query in queries:
        # If the query is of type 1, update the frequency of the number
        if query[0] == 1:
            freq[query[1]] -= 1
            freq[query[2]] += 1
        # If the query is of type 2, find the length of the shortest contiguous subarray
        else:
            # Initialize the minimum length and the current length to 0
            min_len = 0
            curr_len = 0
            # Iterate through the numbers from 1 to K
            for num in range(1, K + 1):
                # If the current number is in the frequency dictionary and its frequency is greater than 0, increment the current length
                if num in freq and freq[num] > 0:
                    curr_len += 1
                # If the current number is not in the frequency dictionary or its frequency is 0, reset the current length to 0
                else:
                    curr_len = 0
                # If the current length is greater than the minimum length, update the minimum length
                if curr_len > min_len:
                    min_len = curr_len
            # If the minimum length is 0, return -1 because no contiguous subarray contains all numbers from 1 to K
            if min_len == 0:
                print(-1)
            # Otherwise, return the minimum length
            else:
                print(min_len)

if __name__ == "__main__":
    N, K, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    for _ in range(M):
        queries.append(list(map(int, input().split())))
    solve(arr, queries)

