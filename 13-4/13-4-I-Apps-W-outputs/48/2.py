
def solve(arr):
    count = 0
    while arr:
        count += 1
        temp = []
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                temp.append(arr[i])
        for i in temp:
            arr.remove(i)
    return count

