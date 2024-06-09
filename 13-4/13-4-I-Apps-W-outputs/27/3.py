
def get_distinct_subsequences(arr):
    n = len(arr)
    if n == 0:
        return 1
    else:
        return (get_distinct_subsequences(arr[1:]) + get_distinct_subsequences(arr[1:])) % 1000000007

def solve(n, m):
    arr = list(range(1, m+1))
    return get_distinct_subsequences(arr) % 1000000007

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve(n, m))

