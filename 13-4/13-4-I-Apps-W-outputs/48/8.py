
def solve(arr):
    count = 0
    while arr:
        count += 1
        arr = [arr[0]] + [x for x in arr[1:] if x != arr[0]]
    return count

