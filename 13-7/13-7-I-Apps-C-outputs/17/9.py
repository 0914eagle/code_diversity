
def get_magical_subarray(arr, l, r):
    # Find the maximum length of the subarray
    max_len = r - l + 1
    
    # Find the minimum and maximum values in the subarray
    min_val = arr[l]
    max_val = arr[l]
    for i in range(l+1, r+1):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
    
    # Check if the subarray is magical
    if min_val <= max_val:
        return max_len
    
    # If the subarray is not magical, return 0
    return 0

def solve(arr, queries):
    result = []
    for query in queries:
        l, r = query
        result.append(get_magical_subarray(arr, l, r))
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    result = solve(arr, queries)
    for i in result:
        print(i)

