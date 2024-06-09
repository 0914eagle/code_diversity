
def is_ladder(arr, l, r):
    if l == r:
        return True
    if l + 1 == r:
        return arr[l] == arr[r]
    if arr[l] != arr[r]:
        return False
    return is_ladder(arr, l + 1, r - 1)

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(m):
    l, r = map(int, input().split())
    if is_ladder(arr, l, r):
        print("Yes")
    else:
        print("No")

