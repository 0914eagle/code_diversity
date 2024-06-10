
def get_magical_subarray(arr, l, r):
    # Find the longest contiguous subarray with the property of being magical
    max_length = 0
    for i in range(l, r+1):
        if arr[i] >= arr[l] and arr[i] <= arr[r]:
            length = 1
            for j in range(i+1, r+1):
                if arr[j] >= arr[l] and arr[j] <= arr[r]:
                    length += 1
            max_length = max(max_length, length)
    return max_length

def solve(arr, queries):
    # Iterate through the queries and find the longest contiguous subarray for each query
    results = []
    for query in queries:
        l, r = query[0]-1, query[1]-1
        results.append(get_magical_subarray(arr, l, r))
    return results

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    print(*solve(arr, queries))

