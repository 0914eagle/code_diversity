
def is_ladder(arr, l, r):
    if l == r:
        return True
    if l + 1 == r and arr[l] == arr[r]:
        return True
    if arr[l] <= arr[l + 1] and arr[l + 1] <= arr[l + 2]:
        return is_ladder(arr, l + 1, r)
    if arr[l] >= arr[l + 1] and arr[l + 1] >= arr[l + 2]:
        return is_ladder(arr, l + 1, r)
    return False

def solve(arr, queries):
    for l, r in queries:
        if is_ladder(arr, l, r):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    for _ in range(m):
        l, r = map(int, input().split())
        queries.append((l, r))
    solve(arr, queries)

