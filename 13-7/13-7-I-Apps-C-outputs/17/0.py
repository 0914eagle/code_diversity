
def get_magical_subarray(array, l, r):
    # Find the first and last number in the subarray
    first_num = array[l-1]
    last_num = array[r-1]
    
    # Initialize the length of the longest magical subarray as 0
    longest_magical_subarray = 0
    
    # Iterate through the subarray and find the longest magical subarray
    for i in range(l, r+1):
        # Check if the current subarray is magical
        if array[i-1] >= first_num and array[i-1] <= last_num:
            # If the current subarray is magical, update the length of the longest magical subarray
            longest_magical_subarray = max(longest_magical_subarray, i-l+1)
    
    return longest_magical_subarray

def solve(array, queries):
    result = []
    for l, r in queries:
        result.append(get_magical_subarray(array, l, r))
    return result

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        l, r = map(int, input().split())
        queries.append((l, r))
    result = solve(array, queries)
    for i in result:
        print(i)

