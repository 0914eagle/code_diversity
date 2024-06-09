
def is_ladder(arr, l, r):
    if l == r:
        return True
    if l + 1 == r:
        return arr[l] == arr[r]
    if arr[l] != arr[r]:
        return False
    return is_ladder(arr, l + 1, r - 1)

def solve(arr, queries):
    for l, r in queries:
        print("Yes") if is_ladder(arr, l, r) else print("No")

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    for _ in range(m):
        l, r = map(int, input().split())
        queries.append((l, r))
    solve(arr, queries)

