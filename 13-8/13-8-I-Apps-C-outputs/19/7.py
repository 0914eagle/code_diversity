
def get_magical_subarray(array, l, r):
    # Find the minimum and maximum values in the subarray
    min_val = min(array[l:r+1])
    max_val = max(array[l:r+1])
    
    # Iterate through the subarray and count the number of elements that are between the minimum and maximum values
    count = 0
    for i in range(l, r+1):
        if array[i] >= min_val and array[i] <= max_val:
            count += 1
    
    return count

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
        queries.append(list(map(int, input().split())))
    result = solve(array, queries)
    for i in result:
        print(i)

