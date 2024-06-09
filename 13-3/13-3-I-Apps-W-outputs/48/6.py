
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


n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(m):
    l, r = map(int, input().split())
    if is_ladder(arr, l - 1, r - 1):
        print("Yes")
    else:
        print("No")

