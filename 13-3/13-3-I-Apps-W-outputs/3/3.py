
def solve(arr):
    count = 0
    while arr:
        count += 1
        temp = []
        for i in range(len(arr)):
            if arr[i] != arr[i-1] or i == 0:
                temp.append(arr[i])
        arr = temp
    return count

