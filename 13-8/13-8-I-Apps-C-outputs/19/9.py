
def get_magical_subarray(arr, l, r):
    # Find the smallest and largest elements in the subarray
    smallest = arr[l]
    largest = arr[l]
    for i in range(l+1, r+1):
        if arr[i] < smallest:
            smallest = arr[i]
        if arr[i] > largest:
            largest = arr[i]
    
    # Return the length of the subarray if all elements are between the smallest and largest elements
    if all(smallest <= x <= largest for x in arr[l:r+1]):
        return r - l + 1
    
    # Return 0 if the subarray is not magical
    return 0

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
        queries.append(list(map(int, input().split())))
    result = solve(arr, queries)
    for i in result:
        print(i)

if __name__ == '__main__':
    main()

