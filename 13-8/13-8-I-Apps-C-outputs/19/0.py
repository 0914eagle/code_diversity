
def get_magical_subarray(arr, l, r):
    max_len = 0
    for i in range(l, r+1):
        for j in range(i, r+1):
            if is_magical(arr[i:j+1]):
                max_len = max(max_len, j-i+1)
    return max_len

def is_magical(arr):
    return arr[0] <= arr[-1] and all(l <= x <= r for x in arr)

def solve(arr, queries):
    return [get_magical_subarray(arr, l, r) for l, r in queries]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    print(*solve(arr, queries), sep='\n')

