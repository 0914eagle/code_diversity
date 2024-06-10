
def get_magical_subarray_length(array, l, r):
    # Find the smallest and largest elements in the subarray
    smallest = min(array[l:r+1])
    largest = max(array[l:r+1])
    
    # Return the length of the subarray if all elements are between the smallest and largest elements
    if all(smallest <= x <= largest for x in array[l:r+1]):
        return r - l + 1
    else:
        return 0

def solve(array, queries):
    result = []
    for l, r in queries:
        result.append(get_magical_subarray_length(array, l, r))
    return result

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    result = solve(array, queries)
    for x in result:
        print(x)

