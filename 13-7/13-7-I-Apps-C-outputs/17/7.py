
def get_magical_subarray(arr, l, r):
    # Find the smallest and largest elements in the subarray
    smallest = min(arr[l:r+1])
    largest = max(arr[l:r+1])
    
    # Initialize the length of the longest magical subarray as 0
    max_length = 0
    
    # Iterate over the subarray and check if the elements are between the smallest and largest elements
    for i in range(l, r+1):
        if smallest <= arr[i] <= largest:
            max_length = max(max_length, i-l+1)
    
    return max_length

def solve(arr, queries):
    result = []
    for l, r in queries:
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

