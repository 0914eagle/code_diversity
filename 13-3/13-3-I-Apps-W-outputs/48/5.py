
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

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(m):
    l, r = map(int, input().split())
    if is_ladder(arr, l - 1, r - 1):
        print("Yes")
    else:
        print("No")

