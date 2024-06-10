
def is_magical(arr):
    return all(arr[0] <= x <= arr[-1] for x in arr)

def get_longest_magical_subarray(arr, l, r):
    longest = 0
    for i in range(l, r+1):
        subarr = arr[i:r+1]
        if is_magical(subarr) and len(subarr) > longest:
            longest = len(subarr)
    return longest

def solve(arr, queries):
    return [get_longest_magical_subarray(arr, l, r) for l, r in queries]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    queries = [[int(x) for x in input().split()] for _ in range(q)]
    print(*solve(arr, queries))

