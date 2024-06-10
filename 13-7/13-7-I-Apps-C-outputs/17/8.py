
def get_magical_subarray(arr, l, r):
    # Find the smallest and largest elements in the subarray
    smallest = min(arr[l:r+1])
    largest = max(arr[l:r+1])
    
    # Check if all elements are between the smallest and largest element
    if all(smallest <= x <= largest for x in arr[l:r+1]):
        return r - l + 1
    else:
        return 0

def solve(arr, queries):
    result = []
    for l, r in queries:
        result.append(get_magical_subarray(arr, l, r))
    return result

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    result = solve(arr, queries)
    for x in result:
        print(x)

