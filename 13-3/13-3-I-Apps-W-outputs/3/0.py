
def solve(arr):
    count = 0
    while arr:
        temp = []
        for i in range(len(arr)):
            if arr[i] != arr[i-1] and arr[i] in temp:
                break
            temp.append(arr[i])
        count += 1
        arr = arr[len(temp):]
    return count

