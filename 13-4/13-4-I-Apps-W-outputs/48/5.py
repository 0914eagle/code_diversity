
def solve(arr):
    count = 0
    while arr:
        count += 1
        curr = arr[0]
        arr = [x for x in arr if x != curr]
    return count

