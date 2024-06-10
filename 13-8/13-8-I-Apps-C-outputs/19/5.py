
def get_magical_subarray(arr, l, r):
    # Find the minimum and maximum values in the subarray
    min_val = min(arr[l:r+1])
    max_val = max(arr[l:r+1])
    
    # Initialize the length of the longest contiguous subarray as 0
    max_len = 0
    
    # Iterate through the subarray and find the longest contiguous subarray with the property that all values are between the minimum and maximum values
    for i in range(l, r+1):
        if arr[i] >= min_val and arr[i] <= max_val:
            curr_len = i - l + 1
            if curr_len > max_len:
                max_len = curr_len
    
    return max_len

def solve(arr, queries):
    result = []
    for l, r in queries:
        result.append(get_magical_subarray(arr, l, r))
    return result

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        l, r = map(int, input().split())
        queries.append((l, r))
    result = solve(arr, queries)
    for i in result:
        print(i)

if __name__ == '__main__':
    main()

