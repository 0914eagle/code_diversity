
def is_ladder(arr, l, r):
    if l == r:
        return True
    if l + 1 == r and arr[l] == arr[r]:
        return True
    if arr[l] > arr[r]:
        return False
    for i in range(l + 1, r):
        if arr[i] < arr[l] or arr[i] > arr[r]:
            return False
    return True


def solve(arr, queries):
    for l, r in queries:
        if is_ladder(arr, l, r):
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().split())))
    solve(arr, queries)

