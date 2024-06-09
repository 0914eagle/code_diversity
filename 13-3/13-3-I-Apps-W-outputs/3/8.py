
def solve(arr):
    count = 0
    while arr:
        temp = []
        for i in range(len(arr)):
            if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
                temp.append(arr[i])
        arr = temp
        count += 1
    return count

